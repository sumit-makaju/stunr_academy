from django.contrib import admin
from .models import Customer
# Register your models here.

 
 
 
 
 
admin.site.site_header = 'Hidden Action'
admin.site.index_title = 'Stunt Academy'
@admin.register(Customer)
 
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','password','role')