from django.db import models

# Create your models here.
class Teacher(models.Model):
    name    =models.CharField(max_length=50,null=True)
    age     =models.IntegerField(null=True)
    gender  =models.CharField(max_length=1)
    pic     =models.ImageField(upload_to='MEDIA_ROOT',null=True,blank=True)
    sub     =models.CharField(max_length=3,null=True)
