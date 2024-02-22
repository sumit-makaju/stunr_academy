from django.db import models

# Create your models here.

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    package_type = models.CharField(max_length=20)
    hostel= models.CharField(max_length=300)
    insurance = models.CharField(max_length=20)
    riding_gears =models.CharField(max_length=20)
    trainer_experience = models.CharField(max_length=100)
    hours_num = models.CharField(max_length=200)
    price = models.BigIntegerField(default=None, blank=True, null=True)
    
    # def __str__(self):
    #     return self.name

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    trainer_id = models.IntegerField()
    package_id = models.IntegerField()
    advance_amount = models.BigIntegerField()
   
    