from django.db import models
from django.db.models.fields import CharField



# Create your models here.

class event(models.Model):

    gender_choices=(
        ('M','male'),
        ('F', 'female'),
        ('N-B','non-binary'),
        ('N/A','prefer not to say')
    )


    title = models.CharField(max_length=50,null=False)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    gender = models.CharField(max_length=11,choices=gender_choices,null=True,blank=True)
    description = models.CharField(max_length=150,null=False)
    
    def __str__(self):
        return self.title

     


    