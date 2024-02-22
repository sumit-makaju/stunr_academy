from django.contrib import admin
from .models import Package
# Register your models here.
@admin.register(Package)
 
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id','package_type','hostel','insurance','riding_gears','trainer_experience','hours_num')