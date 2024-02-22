from django.contrib import admin
from .models import Trainer
# Register your models here.


@admin.register(Trainer)
 
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','password','confirm_password')