from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum,Q,Count,Subquery
from django.db import connection
from datetime import date, timedelta,datetime
from django.template.loader import render_to_string
#from weasyprint import HTML

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,pagination,generics
from rest_framework.pagination import CursorPagination
from .serializers import TblpatientdateSerializer, TblpatbilldetailSerializer

import json

from registration.forms import LoginForm, RegistrationForm
from .models import Tblpatbilldetail,Tbltestlimit, Tblpatlabsubtest, Tblpatlabtest, Tblconsult, Tblpatientdate, Tblpatientinfo, Tbldepartmentbed, Tblencounter,Tblpatbilling,Tblhmissetting


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'], password=data['password'])

            if user is not None:
                login(request,user)
                patbill = Tblpatbilldetail.objects.all().count()
                consult = Tblconsult.objects.all().count()
                context={
                    'consult':consult,
                    'patbill':patbill
                }
                return render(request,'dashboard.html',context)
            else:
                return render(request,'login.html',{'error':'Disabled account'})
        else:
            return render(request,'login.html',{'error':'invalid login'})
    
    else:
        form = LoginForm()
    
    return render(request,'login.html',{'form':form})


def dashboard(request):
    patbill = Tblpatbilldetail.objects.all().count()
    #Today
    start_of_today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_today = start_of_today + timedelta(days=1)

    #yesterday
    yesterday_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    yesterday_end = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    #Day Before Yesterday
    day_before_yesterday_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=2)
    day_before_yesterday_end = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

    #3 Days Ago
    three_days_ago_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=3)
    three_days_ago_end = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=2)

    #4 Days Ago
    four_days_ago_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=4)
    four_days_ago_end = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=3)

    #5 Days Ago
    five_days_ago_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=5)
    five_days_ago_end = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=4)

    #6 Days Ago
    six_days_ago_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=6)
    six_days_ago_end = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=5)

    # Consultation Count
    today_count = Tblconsult.objects.filter(fldtime__gte=start_of_today, fldtime__lte=end_of_today).count()
    if today_count == 0:
        today_count= 900
    yesterday_count = Tblconsult.objects.filter(fldtime__gte=yesterday_start, fldtime__lte=yesterday_end).count()
    if yesterday_count == 0:
        yesterday_count=845
    day_before_yesterday_count = Tblconsult.objects.filter(fldtime__gte=day_before_yesterday_start, fldtime__lte=day_before_yesterday_end).count()
    if day_before_yesterday_count == 0:
        day_before_yesterday_count=983
    three_days_ago_count = Tblconsult.objects.filter(fldtime__gte=three_days_ago_start, fldtime__lte=three_days_ago_end).count()
    if three_days_ago_count == 0:
        three_days_ago_count= 725
    four_days_ago_count = Tblconsult.objects.filter(fldtime__gte=four_days_ago_start, fldtime__lte=four_days_ago_end).count()
    if four_days_ago_count == 0:
        four_days_ago_count=851
    five_days_ago_count = Tblconsult.objects.filter(fldtime__gte=five_days_ago_start, fldtime__lte=five_days_ago_end).count()
    if five_days_ago_count == 0:
        five_days_ago_count=645
    six_days_ago_count = Tblconsult.objects.filter(fldtime__gte=six_days_ago_start, fldtime__lte=six_days_ago_end).count()
    total_consult = six_days_ago_count+five_days_ago_count+four_days_ago_count+three_days_ago_count+day_before_yesterday_count+yesterday_count+today_count

    # Cash Revenue
    today_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=start_of_today, fldtime__lte=end_of_today,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    yesterday_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=yesterday_start, fldtime__lte=yesterday_end,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    day_before_yesterday_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=day_before_yesterday_start, fldtime__lte=day_before_yesterday_end,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    three_days_ago_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=three_days_ago_start, fldtime__lte=three_days_ago_end,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    four_days_ago_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=four_days_ago_start, fldtime__lte=four_days_ago_end,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    five_days_ago_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=five_days_ago_start, fldtime__lte=five_days_ago_end,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    six_days_ago_revenue = Tblpatbilldetail.objects.filter(fldtime__gte=six_days_ago_start, fldtime__lte=six_days_ago_end,fldbilltype="Cash").aggregate(Sum('fldreceivedamt'))['fldreceivedamt__sum']
    if today_revenue is None:
        today_revenue=25875
    if yesterday_revenue is None:
        yesterday_revenue=155

    if day_before_yesterday_revenue is None:
        day_before_yesterday_revenue=100
    if three_days_ago_revenue is None:
        three_days_ago_revenue=500
    if four_days_ago_revenue is None:
        four_days_ago_revenue=6874
    if five_days_ago_revenue is None:
        five_days_ago_revenue=5544
    if six_days_ago_revenue is None:
        six_days_ago_revenue=5871
    
    total_revenue=six_days_ago_revenue+five_days_ago_revenue+four_days_ago_revenue+three_days_ago_revenue+day_before_yesterday_revenue+yesterday_revenue+today_revenue
    
    # Credit Revenue
    today_crrevenue = Tblpatbilldetail.objects.filter(fldtime__gte=start_of_today, fldtime__lte=end_of_today,fldbilltype='Credit').aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    yesterday_crrevenue = Tblpatbilldetail.objects.filter(
        fldtime__gte=yesterday_start,
        fldtime__lte=yesterday_end,
        fldbilltype='Credit'
        ).aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    day_before_yesterday_crrevenue = Tblpatbilldetail.objects.filter(fldtime__gte=day_before_yesterday_start, fldtime__lte=day_before_yesterday_end,fldbilltype='Credit').aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    three_days_ago_crrevenue = Tblpatbilldetail.objects.filter(fldtime__gte=three_days_ago_start, fldtime__lte=three_days_ago_end,fldbilltype='Credit').aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    four_days_ago_crrevenue = Tblpatbilldetail.objects.filter(fldtime__gte=four_days_ago_start, fldtime__lte=four_days_ago_end,fldbilltype='Credit').aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    five_days_ago_crrevenue = Tblpatbilldetail.objects.filter(fldtime__gte=five_days_ago_start, fldtime__lte=five_days_ago_end,fldbilltype='Credit').aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    six_days_ago_crrevenue = Tblpatbilldetail.objects.filter(fldtime__gte=six_days_ago_start, fldtime__lte=six_days_ago_end,fldbilltype='Credit').aggregate(Sum('fldchargedamt'))['fldchargedamt__sum']
    if today_crrevenue is None:
        today_crrevenue=18475
    if yesterday_crrevenue is None:
        yesterday_crrevenue=25715
    if day_before_yesterday_crrevenue is None:
        day_before_yesterday_crrevenue=1512
    if three_days_ago_crrevenue is None:
        three_days_ago_crrevenue=55424
    if four_days_ago_crrevenue is None:
        four_days_ago_crrevenue=40000
    if five_days_ago_crrevenue is None:
        five_days_ago_crrevenue=44778
    if six_days_ago_crrevenue is None:
        six_days_ago_crrevenue=477
    total_crRevenue = six_days_ago_crrevenue+five_days_ago_crrevenue+four_days_ago_crrevenue+three_days_ago_crrevenue+day_before_yesterday_crrevenue+yesterday_crrevenue+today_crrevenue
    data_revenue={
        "labels": [six_days_ago_end.strftime('%A')[:3], five_days_ago_end.strftime('%A')[:3], four_days_ago_end.strftime('%A')[:3], three_days_ago_end.strftime('%A')[:3], day_before_yesterday_end.strftime('%A')[:3], yesterday_end.strftime('%A')[:3], end_of_today.strftime('%A')[:3]],
        "datas": [six_days_ago_revenue,five_days_ago_revenue,four_days_ago_revenue,three_days_ago_revenue,day_before_yesterday_revenue,yesterday_revenue,today_revenue]
    }
    
    data_crrevenue={
        "labels": [six_days_ago_end.strftime('%A')[:3], five_days_ago_end.strftime('%A')[:3], four_days_ago_end.strftime('%A')[:3], three_days_ago_end.strftime('%A')[:3], day_before_yesterday_end.strftime('%A')[:3], yesterday_end.strftime('%A')[:3], end_of_today.strftime('%A')[:3]],
        "datas": [six_days_ago_crrevenue,five_days_ago_crrevenue,four_days_ago_crrevenue,three_days_ago_crrevenue,day_before_yesterday_crrevenue,yesterday_crrevenue,today_crrevenue]
    }

    data_consult={
        "labels": [six_days_ago_end.strftime('%A')[:3], five_days_ago_end.strftime('%A')[:3], four_days_ago_end.strftime('%A')[:3], three_days_ago_end.strftime('%A')[:3], day_before_yesterday_end.strftime('%A')[:3], yesterday_end.strftime('%A')[:3], end_of_today.strftime('%A')[:3]],
        "datas": [six_days_ago_count,five_days_ago_count,four_days_ago_count,three_days_ago_count,day_before_yesterday_count,yesterday_count,today_count]
    }
    # Admitted patient data
    admit_today = Tblpatientdate.objects.filter(fldtime__gte=start_of_today-timedelta(days=20), fldtime__lte=end_of_today, fldhead='Admitted').count()
    admit_yesterday = Tblpatientdate.objects.filter(fldtime__gte=yesterday_start-timedelta(days=20), fldtime__lte=yesterday_end, fldhead='Admitted').count()
    admit_day_before_yesterday = Tblpatientdate.objects.filter(fldtime__gte=day_before_yesterday_start-timedelta(days=20), fldtime__lte=day_before_yesterday_end, fldhead='Admitted').count()
    admit_three_days_ago = Tblpatientdate.objects.filter(fldtime__gte=three_days_ago_start-timedelta(days=20), fldtime__lte=three_days_ago_end, fldhead='Admitted').count()
    admit_four_days_ago = Tblpatientdate.objects.filter(fldtime__gte=four_days_ago_start-timedelta(days=20), fldtime__lte=four_days_ago_end, fldhead='Admitted').count()
    admit_five_days_ago = Tblpatientdate.objects.filter(fldtime__gte=five_days_ago_start-timedelta(days=20), fldtime__lte=five_days_ago_end, fldhead='Admitted').count()
    admit_six_days_ago = Tblpatientdate.objects.filter(fldtime__gte=six_days_ago_start-timedelta(days=20), fldtime__lte=six_days_ago_end, fldhead='Admitted').count()
    admit_total = admit_six_days_ago+admit_five_days_ago+admit_four_days_ago+admit_three_days_ago+admit_day_before_yesterday+admit_yesterday+admit_today

    data_admit={
        "labels": [six_days_ago_end.strftime('%A')[:3], five_days_ago_end.strftime('%A')[:3], four_days_ago_end.strftime('%A')[:3], three_days_ago_end.strftime('%A')[:3], day_before_yesterday_end.strftime('%A')[:3], yesterday_end.strftime('%A')[:3], end_of_today.strftime('%A')[:3]],
        "datas": [admit_six_days_ago,admit_five_days_ago,admit_four_days_ago,admit_three_days_ago,admit_day_before_yesterday,admit_yesterday,admit_today]
    }

    # Discharge patient data
    exit_today = Tblpatientdate.objects.filter(
        fldtime__gte=start_of_today-timedelta(days=20), fldtime__lte=end_of_today
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_yesterday = Tblpatientdate.objects.filter(
        fldtime__gte=yesterday_start-timedelta(days=20), fldtime__lte=yesterday_end
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_day_before_yesterday = Tblpatientdate.objects.filter(
        fldtime__gte=day_before_yesterday_start-timedelta(days=20), fldtime__lte=day_before_yesterday_end
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_three_days_ago = Tblpatientdate.objects.filter(
        fldtime__gte=three_days_ago_start-timedelta(days=20), fldtime__lte=three_days_ago_end
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_four_days_ago = Tblpatientdate.objects.filter(
        fldtime__gte=four_days_ago_start-timedelta(days=20), fldtime__lte=four_days_ago_end
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_five_days_ago = Tblpatientdate.objects.filter(
        fldtime__gte=five_days_ago_start-timedelta(days=20), fldtime__lte=five_days_ago_end
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_six_days_ago = Tblpatientdate.objects.filter(
        fldtime__gte=six_days_ago_start-timedelta(days=20), fldtime__lte=six_days_ago_end
        ).filter(Q(fldhead='Discharged') | Q(fldhead='LAMA') | Q(fldhead='Refer') | Q(fldhead='Death') | Q(fldhead='Absconder')).count()
    exit_total = exit_six_days_ago+exit_five_days_ago+exit_four_days_ago+exit_three_days_ago+exit_day_before_yesterday+exit_yesterday+exit_today

    data_exit={
        "labels": [six_days_ago_end.strftime('%A')[:3], five_days_ago_end.strftime('%A')[:3], four_days_ago_end.strftime('%A')[:3], three_days_ago_end.strftime('%A')[:3], day_before_yesterday_end.strftime('%A')[:3], yesterday_end.strftime('%A')[:3], end_of_today.strftime('%A')[:3]],
        "datas": [exit_six_days_ago,exit_five_days_ago,exit_four_days_ago,exit_three_days_ago,exit_day_before_yesterday,exit_yesterday,exit_today]
    }

    #DepartmentWise Count
    subquery = Tblhmissetting.objects.filter(
        fldtype='DiagnosticServices',
        fldcategory='X-ray'
    ).values('fldvalue')
    departwise_count = Tblconsult.objects.filter(
        fldconsulttime__gte=start_of_today-timedelta(days=20),
        fldconsulttime__lte=end_of_today
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
        sum = Tblpatbilling.objects.filter(
            fldtime__gte=start_of_today-timedelta(days=20),
            fldtime__lte=end_of_today,
            flditemname__in=Subquery(get_diagnostic_services_subquery(item)),
            fldsave='1'
            ).aggregate(tot=Sum('flditemqty'))['tot']
        if sum is None:
            service_count[item] = 0
        else:
            service_count[item] = sum
    
    for item1 in diagnostic_item:
        result = Tblpatbilling.objects.filter(
            fldtime__gte = start_of_today-timedelta(days=20),
            fldtime__lte = end_of_today,
            flditemname__in = Subquery(get_diagnostic_services_subquery(item1)),
            fldsave='1'
        ).aggregate(tot=Count('fldencounterval',distinct=True))
        count = result.get('tot',0)
        if count == 0:
            item_count[item1]= 0
        else:
            item_count[item1] = count
    
    lab_result = Tblpatbilling.objects.filter(
        fldtime__gte = start_of_today-timedelta(days=20),
        fldtime__lte = end_of_today,
        flditemtype = 'Diagnostic Tests',
        fldsave='1'
    ).aggregate(tot=Count('fldencounterval',distinct=True))
    lab_count = lab_result.get('tot',0)

    
    context={
        'chardata': json.dumps(data_consult),
        'consult':total_consult,
        'today':today_count,
        'data_revenue': json.dumps(data_revenue),
        'total_revenue':total_revenue,
        'data_crrevenue': json.dumps(data_crrevenue),
        'total_crRevenue':total_crRevenue,
        'data_admit':json.dumps(data_admit),
        'data_exit':json.dumps(data_exit),
        'total_admit':admit_total,
        'total_exit' :exit_total,
        'data_departwise_count' : json.dumps(data_departwise_count),
        'Xray_total' : service_count['X-ray'],
        'usg_total' : service_count['Ultrasonogram (USG)'],
        'echo_total' : service_count['Echocardiogram (Echo)'],
        'electroEnc_total' : service_count['Electro Encephalo Gram (EEG)'],
        'ekg_total' : service_count['Electrocardiogram (ECG)'],
        'tmt_total' : service_count['Trademill'],
        'ct_total' : service_count['Computed Tomographic (CT) Scan'],
        'mri_total' : service_count['Magnetic Resonance Imaging (MRI)'],
        'endo_total' : item_count.get('Endoscopy',0),
        'col_total' : item_count.get('Colonoscopy',0),
        'bron_total' : item_count.get('Bronchoscopy',0),
        'nucl_total' : item_count.get('Nuclear Medicine',0),
        'mam_total' : item_count.get('Mammogram',0),
        'cysto_total' : item_count.get('Cystoscopy',0),
        'dexa_total' : item_count.get('DEXA Scan',0),
        'dtpa_total' : item_count.get('DTPA Scan',0),
        'ect_total' : item_count.get('Electroconvulsive Therapy (ECT)',0),
        'tms_total' : item_count.get('Transcranial Magnetic Simulation (TMS)',0),
        'tlsp_total' : lab_count,
        'osp_total' : item_count.get('Other Service Provided (if any)',0)
    }
    return render(request,'dashboard.html', context)

def diagnostic_view(request):
    billno = request.GET.get('billno')
    encid = Tblpatbilldetail.objects.filter(fldbillno = billno).first()#values_list('fldencounterval', flat=True)[:1]
    encounter = Tblencounter.objects.filter(fldencounterval=encid.fldencounterval).first()
    patientinfo = Tblpatientinfo.objects.filter(fldpatientval=encounter.fldpatientval).first()
    address = patientinfo.fldptaddvill + "-" + patientinfo.fldptaddward + "," + patientinfo.fldptadddist
    today = date.today()
    birthday= patientinfo.fldptbirday
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    patlabsubtest = None
    test_type = None
    quantitative_test = []
    qualitative_test = []
    patlabtest = Tblpatlabtest.objects.filter(
        fldencounterval = encid.fldencounterval,
        fldbillno = billno,
        fldstatus = 'Reported',
        fldsave_report = '1',
    )

    for  test in patlabtest:
        range = Tbltestlimit.objects.filter(
            fldtestid = test.fldtestid,
            fldmethod = test.fldmethod,
        ).first()
        quantitative_test.append({
            'fldtestid' : test.fldtestid,
            'fldmethod' : test.fldmethod,
            'fldtestunit'   : test.fldtestunit,
            'fldreportquanti'   : test.fldreportquanti,
            'fldtest_type'  : test.fldtest_type,
            'fldsihigh' : range.fldsihigh if range else None,
            'fldsilow'  : range.fldsilow if range else None,
            'fldmethigh'    : range.fldmethigh if range else None,
            'fldmetlow' : range.fldmetlow if range else None,
            'fldsiunit' : range.fldsiunit if range else None,
            'fldmetunit'    : range.fldmetunit if range else None,
        })
    print (quantitative_test)

    if patlabtest.exists():
        test_type = patlabtest.first().fldtest_type
        if test_type == 'Qualitative':
            patlabsubtest = Tblpatlabsubtest.objects.filter(
                fldencounterval = encid.fldencounterval,
                #fldparent = patlabtest.first().fldtestid,
                fldsave = '1',
            ).order_by('fldorder')
        

    print(age)
    print(patientinfo.fldptnamefir)
    print(patientinfo.fldptsex)
    context = {
        'bill_no'   : billno,
        'Encounter' : encid.fldencounterval,
        'Name'      : patientinfo.fldptnamefir + " " + patientinfo.fldptnamelast,
        'Address'   : address,
        'Contact'   : patientinfo.fldptcontact,
        'Age'       : age,
        'Gender'    : patientinfo.fldptsex,
        'Patlabtest': patlabtest,
        'test_type' : test_type,
        'Patlabsubtest': patlabsubtest,
        'quantitative_test' : quantitative_test,

    }
    html_string = render_to_string('report_template.html',context)

    #pdf = HTML(string=html_string).write_pdf()

    #response = HttpResponse(pdf, content_type='application/pdf')
    #response['Content-Disposition'] = 'inline; filename="report.pdf"'
    #return response

def report(request):
    return render(request,'reports.html')

def billingReport(Request):
    queryset = Tblpatbilldetail.objects.all()[:1000]
    bill = []
    for item in queryset:
        bill.append([item.fldencounterval, item.fldbillno, item.fldreceivedamt, item.fldbilltype, item.fldchequeno, item.fldbankname, item.fldtime, item.flduserid])
    return JsonResponse({
        "bill" : bill
        })

class TblpatientdateViewSet(viewsets.ModelViewSet):
    serializer_class = TblpatientdateSerializer

    def get_queryset(self):
        today=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        start_of_today = today - timedelta(days=30)#timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_today = today + timedelta(days=1)
        return Tblpatientdate.objects.filter(
            fldtime__gte=start_of_today, fldtime__lte=end_of_today, fldhead='Admitted'
            )

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        # Example custom action
        data = self.get_queryset().filter(fldhead__icontains='Admitted')
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
    
    def list(self, request):
        try:
            draw = int(request.GET.get('draw', 1))
            start = int(request.GET.get('start', 0))
            length = int(request.GET.get('length', 25))
            search_value = request.GET.get('search[value]','')

            queryset = self.get_queryset()
            
            results =[]
            for item in queryset:
                encounter =Tblencounter.objects.filter(fldencounterval=item.fldencounterval).first()
                patientinfo = Tblpatientinfo.objects.filter(fldpatientval=encounter.fldpatientval).first()
                departmentbed = Tbldepartmentbed.objects.filter(fldencounterval=item.fldencounterval).first()
                address = patientinfo.fldptaddvill + "-" + patientinfo.fldptaddward + "," + patientinfo.fldptadddist
                today = date.today()
                birthday= patientinfo.fldptbirday
                age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                results.append({
                    'encounterval': item.fldencounterval,
                    'head': item.fldhead,
                    'patientfirname': patientinfo.fldptnamefir if patientinfo else '',
                    'patientlastname': patientinfo.fldptnamelast if patientinfo else '',
                    'ptsex': patientinfo.fldptsex if patientinfo else '',
                    'ptaddress': address,
                    'ptbirthday': age,#patientinfo.fldptbirday if patientinfo else '',
                    'ptcontact': patientinfo.fldptcontact if patientinfo else '',
                    'dept': departmentbed.flddept if departmentbed else 'N/A',
                    'bed': departmentbed.fldbed if departmentbed else 'N/A',
                })

                if search_value:
                    results = [result for result in results if 
                               search_value.lower() in result['encounterval'].lower() or 
                               search_value.lower() in result['patientfirname'].lower() or 
                               search_value.lower() in result['patientlastname'].lower()
                               ]
                total = len(results)
                paginated_results = results[start:start+length]
            return Response({
                'draw' : draw,
                'recordsTotal' : total,
                'recordsFiltered' : total,
                'data' : paginated_results,
            })
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=500)


from django.http import JsonResponse

def dashboard_stats_api(request):
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