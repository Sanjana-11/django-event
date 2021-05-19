from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import DateField
from django.db.models.fields import TimeField


# Create your models here.

class event(models.Model):
    title = models.CharField(max_length=50,null=False)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    description = models.CharField(max_length=150,null=False)
    
    def __str__(self):
        return self.title



    