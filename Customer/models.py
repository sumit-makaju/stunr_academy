from django.db import models

# Create your models here.

class Customer(models.Model):
    roles = (
        ('user', 'user'),
        ('trainer', 'trainer'),
    )
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,unique=True)
    phone= models.IntegerField()
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=roles, default='user')
    
    def __str__(self):
        return self.name
  
class CheckIn(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField
    address = models.CharField(max_length=20)
    package_type = models.CharField(max_length=30)
    trainer = models.CharField(max_length=20)
    
     
    def __str__(self):
        return self.name
  

    