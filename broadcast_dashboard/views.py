from django.shortcuts import render
from django.http import JsonResponse

from django.db.models import Sum,Q,Count,Subquery
from django.utils import timezone
from django.db import connection
from datetime import date, timedelta,datetime

from common.models import Tblpatbilldetail,Tbltestlimit, Tblpatlabsubtest, Tblpatlabtest, Tblconsult, Tblpatientdate, Tblpatientinfo, Tbldepartmentbed, Tblencounter,Tblpatbilling,Tblhmissetting


# Create your views here.
def dashboard_stats(request):
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
    
    print(from_date)
    print(to_date)

    total_patients = Tblconsult.objects.filter(fldconsulttime__gte=start_date, fldconsulttime__lte=end_date).count()
    #print (total_patients)
    if total_patients == 0:
        total_patients = 900

    insurance_patients = Tblconsult.objects.filter(fldconsulttime__gte=start_date, fldconsulttime__lte=end_date, fldbillingmode="Health Insurance").count()
    insurance_percentage = int((insurance_patients / total_patients) * 100) if total_patients else 0

    #Get consultation counts by gender
    def get_gender_counts(start_date,end_date):
        from django.db import connection
        
        with connection.cursor() as cursor:
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
    
    def get_insurance_counts(start_date,end_date):
        #from django.db import connection
        
        with connection.cursor() as cursor:
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
    subquery = Tblhmissetting.objects.filter(
        fldtype='DiagnosticServices',
        fldcategory='X-ray'
    ).values('fldvalue')
    departwise_count = Tblconsult.objects.filter(
        fldconsulttime__gte=start_date-timedelta(days=20),
        fldconsulttime__lte=end_date
        ).values('fldconsultname').annotate(cnt=Count('fldid')).order_by('fldconsultname')
    labels = [depart['fldconsultname'] for depart in departwise_count]
    datas = [visit['cnt'] for visit in departwise_count]
    data_departwise_count={
        "labels":labels,
        "datas":datas
    }
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
        return Tblhmissetting.objects.filter(
            fldtype='DiagnosticServices',
            fldcategory=catergory_val
        ).values('fldvalue')
    
    service_count = {}
    item_count = {item: 0 for item in diagnostic_item}

    for item in diagnostic_qty:
        billing_qty = Tblpatbilling.objects.filter(
            fldtime__gte=start_date-timedelta(days=20),
            fldtime__lte=end_date,
            flditemname__in=Subquery(get_diagnostic_services_subquery(item)),
            fldsave='1'
        ).aggregate(tot=Sum('flditemqty'))['tot']
        
        service_count[item] = billing_qty or 0

    for item1 in diagnostic_item:
        result = Tblpatbilling.objects.filter(
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
    
    lab_result = Tblpatbilling.objects.filter(
        fldtime__gte = start_date-timedelta(days=20),
        fldtime__lte = end_date,
        flditemtype = 'Diagnostic Tests',
        fldsave='1'
    ).aggregate(tot=Count('fldencounterval',distinct=True))
    lab_count = lab_result.get('tot',0)
# Bed occupied

    occupied_filter = Q(fldencounterval__isnull=False) & ~Q(fldencounterval="")

    bed_rows = Tbldepartmentbed.objects.filter(
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
    #print(beds)

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
    
    return JsonResponse(data)