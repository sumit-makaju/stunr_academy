from django.db import models

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,unique=True)
    phone= models.IntegerField()
    password = models.CharField(max_length=20)
    confirm_password =models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    