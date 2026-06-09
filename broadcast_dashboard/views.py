import json
import os
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from django.http import JsonResponse

from django.db.models import Sum,Q,Count,Subquery
from django.utils import timezone
from django.db import connections
from datetime import date, timedelta,datetime
import traceback
import logging

from .models import default_dashboard_settings, DashboardSetting
from common.models import Tblconsult, Tbldepartmentbed,Tblpatbilling,Tblhmissetting

LEGACY_DB = "common"

logger =logging.getLogger(__name__)

#Dashboard Helper function
def get_main_dashboard_setting():
    setting, created = DashboardSetting.objects.get_or_create(
        key="main",
        defaults={"value": default_dashboard_settings()}
    )

    # Merge future new settings automatically
    default_value = default_dashboard_settings()
    current_value = setting.value or {}

    merged_value = {
        **default_value,
        **current_value,
    }

    if merged_value != current_value:
        setting.value = merged_value
        setting.save(update_fields=["value", "updated_at"])

    return setting

#CSRF endpoint

@ensure_csrf_cookie
@require_GET
def csrf_token(request):
    return JsonResponse({
        "csrfToken": get_token(request)
    })

# Auth status
@require_GET
def auth_status(request):
    return JsonResponse({
        "authenticated": request.user.is_authenticated,
        "username": request.user.username if request.user.is_authenticated else "",
        "is_staff": request.user.is_staff if request.user.is_authenticated else False,
    })

# Login Api
@csrf_protect
@require_POST
def login_api(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except Exception:
        payload = {}

    username = payload.get("username")
    password = payload.get("password")

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse({
            "success": False,
            "error": "Invalid username or password"
        }, status=400)

    if not user.is_staff:
        return JsonResponse({
            "success": False,
            "error": "You do not have permission to access dashboard settings"
        }, status=403)

    login(request, user)

    return JsonResponse({
        "success": True,
        "username": user.username,
        "is_staff": user.is_staff,
    })

#Logout API
@csrf_protect
@require_POST
def logout_api(request):
    logout(request)

    return JsonResponse({
        "success": True
    })

# Setting API
def dashboard_settings(request):
    setting = get_main_dashboard_setting()

    if request.method == "GET":
        return JsonResponse(setting.value)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({
                "error": "Login required"
            }, status=401)

        if not request.user.is_staff:
            return JsonResponse({
                "error": "Permission denied"
            }, status=403)

        value = setting.value or default_dashboard_settings()

        editable_text_fields = [
            "hospital_name",
            "company_name",
            "theme_color",
            "marquee_text",
        ]

        for field in editable_text_fields:
            if field in request.POST:
                value[field] = request.POST.get(field)

        if "auto_refresh_seconds" in request.POST:
            try:
                value["auto_refresh_seconds"] = int(request.POST.get("auto_refresh_seconds"))
            except Exception:
                value["auto_refresh_seconds"] = 30

        if "show_footer" in request.POST:
            value["show_footer"] = request.POST.get("show_footer") in ["true", "1", "yes", "on"]

        logo_fields = ["hospital_logo", "company_logo"]

        for field in logo_fields:
            uploaded_file = request.FILES.get(field)

            if uploaded_file:
                content_type = uploaded_file.content_type or ""

                if not content_type.startswith("image/"):
                    return JsonResponse({
                        "error": f"{field} must be an image file"
                    }, status=400)

                _, ext = os.path.splitext(uploaded_file.name)
                ext = ext.lower() or ".png"

                file_path = f"dashboard/logos/{field}{ext}"

                if default_storage.exists(file_path):
                    default_storage.delete(file_path)

                saved_path = default_storage.save(file_path, uploaded_file)
                value[field] = default_storage.url(saved_path)

        setting.value = value
        setting.save()

        return JsonResponse({
            "success": True,
            "settings": setting.value
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)

# Dashboard Stats Function Based View
def dashboard_stats(request):
    try:
        # Mocking your core database metrics

        #Today
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        
        if from_date and to_date:
            start_date = timezone.make_aware(
                datetime.strptime(from_date, "%Y-%m-%d")
            )

            end_date = timezone.make_aware(
                datetime.strptime(to_date, "%Y-%m-%d")
            ) + timedelta(days=1)
        else:
            start_date = timezone.now().replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
            end_date = start_date + timedelta(days=1)
    
        print(f"start Date:{from_date},end date: {to_date}")
        
        try:

            total_patients = Tblconsult.objects.using(LEGACY_DB).filter(fldconsulttime__gte=start_date, fldconsulttime__lte=end_date).count()
            print (f"Total Patient: {total_patients}")
        except Exception as db_error:
            print(f"Database error in total_patients: {db_error}")
            return JsonResponse({"error": f"Database error: {str(db_error)}"}, status=500)

        if total_patients == 0:
            total_patients = 900

        insurance_patients = Tblconsult.objects.using(LEGACY_DB).filter(fldconsulttime__gte=start_date, fldconsulttime__lte=end_date, fldbillingmode="Health Insurance").count()
        insurance_percentage = int((insurance_patients / total_patients) * 100) if total_patients else 0

        #Get consultation counts by gender
        def get_gender_counts(start_date,end_date):
            try:
                from django.db import connections
                
                with connections[LEGACY_DB].cursor() as cursor:
                    cursor.execute("""
                        SELECT
                            c.fldconsultname AS dept, 
                            COALESCE(pi.fldptsex, 'Unknown') AS gender,
                            COUNT(*) as count
                        FROM tblconsult c
                        INNER JOIN tblencounter e ON c.fldencounterval = e.fldencounterval
                        INNER JOIN tblpatientinfo pi ON e.fldpatientval = pi.fldpatientval
                        WHERE c.fldconsulttime >= %s
                            AND c.fldconsulttime < %s
                        GROUP BY pi.fldptsex, c.fldconsultname
                    """, [start_date,end_date])
                    
                    rows = cursor.fetchall()
                    #print(rows)
                    results = {}
                    summary = {
                        "total_patients":0,
                        "total_male":0,
                        "total_female":0,
                        "total_unknown":0,
                    }
                    for dept, gender, count in rows:
                        count = int(count or 0)
                        #print(count)
                        if dept not in results:
                            results[dept] = {
                                "count": 0,
                                "Female": 0,
                                "Male": 0,
                                "Unknown": 0,
                                "percentage": 0
                            }
                        
                        results[dept]["count"] += count
                        summary["total_patients"] += count

                    
                        if gender == "Female":
                            results[dept]["Female"] += count
                            summary["total_female"] += count
                        elif gender == "Male":
                            results[dept]["Male"] += count
                            summary["total_male"] += count
                        else:
                            results[dept]["Unknown"] += count
                            summary["total_unknown"] += count
                return {
                    "results":results,
                    "summary":summary,
                }
            except Exception as e:
                print(f"Error in get_gender_counts: {e}")
                traceback.print_exc();
                return {"results": {}, "summary": {"total_patients": 0, "total_male": 0, "total_female": 0, "total_unknown": 0}}
            
        def get_insurance_counts(start_date,end_date):
            try:
                with connections[LEGACY_DB].cursor() as cursor:
                    cursor.execute("""
                        SELECT 
                            COALESCE(e.flddisctype, 'Unknown') AS disctype,
                            COALESCE(pi.fldptsex, 'Unknown') AS gender,
                            COUNT(*) AS count
                        FROM tblconsult c
                        INNER JOIN tblencounter e 
                            ON c.fldencounterval = e.fldencounterval
                        INNER JOIN tblpatientinfo pi 
                            ON e.fldpatientval = pi.fldpatientval
                        WHERE c.fldconsulttime >= %s
                            AND c.fldconsulttime < %s
                        GROUP BY e.flddisctype, pi.fldptsex
                    """, [start_date, end_date])

                    rows = cursor.fetchall()

                results = {}

                for disctype, gender, count in rows:
                    count = int(count or 0)
                    if disctype not in results:
                        results[disctype] = {
                            "count": 0,
                            "Female": 0,
                            "Male": 0,
                            "Unknown": 0,
                            "percentage": 0
                        }

                    results[disctype]["count"] += count
                    #gender_value = str(gender or "").strip().lower()

                    if gender == "Female":
                        results[disctype]["Female"] += count
                    elif gender == "Male":
                        results[disctype]["Male"] += count
                    else:
                        results[disctype]["Unknown"] += count

                total_patients = sum(item["count"] for item in results.values())

                for disctype in results:
                    count = int(results[disctype]["count"] or 0)

                    results[disctype]["percentage"] = round(
                        (count / total_patients) * 100, 2
                    ) if total_patients else 0

                return results
            except Exception as e:
                print(f"Error in get_insurance_counts:{e}")
                traceback.print_exc()
                return{}
        
        gender_counts = get_gender_counts(start_date,end_date)
        #print(gender_counts)
        dept_gender_counts = gender_counts["results"]
        female_count = gender_counts["summary"]["total_female"]
        male_count = gender_counts["summary"]["total_male"]
        insurance_count = get_insurance_counts(start_date,end_date)
        print(insurance_count)

        def calculate_percentage(count, total):
            return round((count / total) * 100, 2) if total else 0
        
        #DepartmentWise Count
        try:
            departwise_count = Tblconsult.objects.using(LEGACY_DB).filter(
                fldconsulttime__gte=start_date-timedelta(days=20),
                fldconsulttime__lte=end_date
                ).values('fldconsultname').annotate(cnt=Count('fldid')).order_by('fldconsultname')
            labels = [depart['fldconsultname'] for depart in departwise_count]
            datas = [visit['cnt'] for visit in departwise_count]
            data_departwise_count={
                "labels":labels,
                "datas":datas
            }
        except Exception as e:
            print(f"Error in department count:{e}")
            data_departwise_count = {"labels": [], "datas": []}

        #Diagnostic Services
        diagnostic_qty = ['X-ray','Ultrasonogram (USG)','Echocardiogram (Echo)','Electro Encephalo Gram (EEG)','Electrocardiogram (ECG)','Trademill','Computed Tomographic (CT) Scan','Magnetic Resonance Imaging (MRI)']
        diagnostic_item = [
            'Endoscopy',
            'Colonoscopy',
            'Bronchoscopy',
            'Nuclear Medicine',
            'Mammogram',
            'Cystoscopy',
            'DEXA Scan',
            'DTPA Scan',
            'Electroconvulsive Therapy (ECT)',
            'Transcranial Magnetic Simulation (TMS)']

        def get_diagnostic_services_subquery(catergory_val):
            return Tblhmissetting.objects.using(LEGACY_DB).filter(
                fldtype='DiagnosticServices',
                fldcategory=catergory_val
            ).values('fldvalue')
        
        service_count = {}
        item_count = {item: 0 for item in diagnostic_item}

        try:
            for item in diagnostic_qty:
                billing_qty = Tblpatbilling.objects.using(LEGACY_DB).filter(
                    fldtime__gte=start_date-timedelta(days=20),
                    fldtime__lte=end_date,
                    flditemname__in=Subquery(get_diagnostic_services_subquery(item)),
                    fldsave='1'
                ).aggregate(tot=Sum('flditemqty'))['tot']
                
                service_count[item] = billing_qty or 0

            for item1 in diagnostic_item:
                result = Tblpatbilling.objects.using(LEGACY_DB).filter(
                    fldtime__gte = start_date-timedelta(days=20),
                    fldtime__lte = end_date,
                    flditemname__in = Subquery(get_diagnostic_services_subquery(item1)),
                    fldsave='1'
                ).aggregate(tot=Count('fldencounterval',distinct=True))
                count = result.get('tot',0)
                if count == 0:
                    item_count[item1]= 0
                else:
                    item_count[item1] = count
            
            lab_result = Tblpatbilling.objects.using(LEGACY_DB).filter(
                fldtime__gte = start_date-timedelta(days=20),
                fldtime__lte = end_date,
                flditemtype = 'Diagnostic Tests',
                fldsave='1'
            ).aggregate(tot=Count('fldencounterval',distinct=True))
            lab_count = lab_result.get('tot',0)
        except Exception as e:
            print(f"Error in diagnostic services: {e}")
            service_count = {item: 0 for item in diagnostic_qty}
            lab_count = 0
        # Bed occupied
        try:
            occupied_filter = Q(fldencounterval__isnull=False) & ~Q(fldencounterval="")
            bed_rows = Tbldepartmentbed.objects.using(LEGACY_DB).filter(
                fldstatus="Active"
            ).values(
                "flddept"
            ).annotate(
                total=Count("fldbed"),
                occupied=Count("fldbed", filter=occupied_filter)
            ).order_by("flddept")

            beds = []

            for row in bed_rows:
                total = row["total"] or 0
                occupied = row["occupied"] or 0
                vacant = total - occupied

                beds.append({
                    "name": row["flddept"],
                    "total": total,
                    "occupied": occupied,
                    "vacant": vacant,
                    "pct": round((occupied / total) * 100, 2) if total else 0
                })
        except Exception as e:
            print(f"Error in bed occupancy: {e}")
            beds = []

        data = {
            "dateFrom": start_date,
            "dateTo": end_date,
            "demographics": {
                "total": total_patients,
                "female": {
                    "count": female_count,
                    "percentage": int((female_count / total_patients) * 100) if total_patients else 0
                },
                "male": {
                    "count": male_count,
                    "percentage": int((male_count / total_patients) * 100) if total_patients else 0
                },
                "insuranceCoverage": {
                    "percentage": insurance_percentage, 
                    "count": insurance_patients
                }
            },
            "paymentTypes": insurance_count,
            "diagnostics": [
                { "name": "X-ray", "count": service_count['X-ray'] }, 
                { "name": "Ultrasonogram (USG)", "count": service_count['Ultrasonogram (USG)'] }, 
                { "name": "Echocardiogram (Echo)", "count": service_count['Echocardiogram (Echo)'] }, 
                { "name": "Electro Encephalo Gram (EEG)", "count": service_count['Electro Encephalo Gram (EEG)'] },
                { "name": "Electrocardiogram (ECG)", "count": service_count['Electrocardiogram (ECG)'] }, 
                { "name": "Trademill", "count": service_count['Trademill'] },
                { "name": "Computed Tomographic (CT) Scan", "count": service_count['Computed Tomographic (CT) Scan'] },
                { "name": "Magnetic Resonance Imaging (MRI)", "count": service_count['Magnetic Resonance Imaging (MRI)'] },
                { "name": "Endoscopy", "count": item_count.get('Endoscopy',0) },
                { "name": "Colonoscopy", "count": item_count.get('Colonoscopy',0) },
                { "name": "Bronchoscopy", "count": item_count.get('Bronchoscopy',0) },
                { "name": "Nuclear Medicine", "count": item_count.get('Nuclear Medicine',0) },
                { "name": "Mammogram", "count": item_count.get('Mammogram',0) },
                { "name": "Cystoscopy", "count": item_count.get('Cystoscopy',0) },
                { "name": "DEXA Scan", "count": item_count.get('DEXA Scan',0) },
                { "name": "DTPA Scan", "count": item_count.get('DTPA Scan',0) },
                { "name": "Electroconvulsive Therapy (ECT)", "count": item_count.get('Electroconvulsive Therapy (ECT)',0) },
                { "name": "Transcranial Magnetic Simulation (TMS)", "count": item_count.get('Transcranial Magnetic Simulation (TMS)',0) },
                { "name": "Total Laboratory Services Provided", "count": lab_count },            
                { "name": "Others", "count": item_count.get('Other Service Provided (if any)',0) },


            ],
            "consultations": dept_gender_counts,
            "beds": beds,
        }
        
        return JsonResponse(data, safe=False)

    except Exception as e:
        print(f"Unexpected error in dashboard_stats: {e}")
        traceback.print_exc()
        return JsonResponse({"error": f"Server error: {str(e)}"}, status=500)