from django.contrib import admin
from .models import Tblpatbilldetail

# Register your models here.
@admin.register(Tblpatbilldetail)
class TblpatbilldetailAdmin(admin.ModelAdmin):
    list_display= [field.name for field in Tblpatbilldetail._meta.get_fields()]

