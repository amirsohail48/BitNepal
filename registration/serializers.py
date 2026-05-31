from rest_framework import serializers
from common.models import Tblpatientdate, Tblpatientinfo, Tbldepartmentbed, Tblpatbilldetail, Tblencounter

class TblpatientdateSerializer(serializers.ModelSerializer):
    fldptnamefir = serializers.CharField(source='tblpatientinfo.fldptnamefir', read_only=True)
    fldptnamelast = serializers.CharField(source='tblpatientinfo.fldptnamelast', read_only=True)
    fldptsex = serializers.CharField(source='tblpatientinfo.fldptsex', read_only=True)
    fldptadddist = serializers.CharField(source='tblpatientinfo.fldptadddist', read_only=True)
    fldptbirday = serializers.CharField(source='tblpatientinfo.fldptbirday', read_only=True)
    fldptcontact = serializers.CharField(source='tblpatientinfo.fldptcontact', read_only=True)
    fldbed = serializers.CharField(source='tblpatientdate.fldbed', read_only=True)
    flddept = serializers.CharField(source='tblpatientdate.flddept', read_only=True)

    class Meta:
        model = Tblpatientdate
        fields = '__all__'

class TblencounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblencounter
        fields = '__all__'
    
class TblpatientinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatientinfo
        fields = '__all__'

class TbldepartmentbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldepartmentbed
        fields = '__all__'

class TblpatbilldetailSerializer(serializers.ModelSerializer):
    #encounter = TblencounterSerializer(source='fldencounterval', read_only=True)
    #patientinfo = serializers.SerializerMethodField()

    class Meta:
        model = Tblpatbilldetail
        fields = '__all__'

    def get_patientinfo(self,obj):
        encounter = Tblencounter.objects.filter(fldencounterval=obj.fldencounterval).first()
        if encounter:
            patientinfo = Tblpatientinfo.objects.filter(fldpatientval=encounter.fldpatientval).first()
        
        if patientinfo:
            return {
                'firstName' : patientinfo.fldptnamefir,
                'lastName' : patientinfo.fldptnamelast
            }
        return {}
    
class TblpatientinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatientinfo
        fields = '__all__'