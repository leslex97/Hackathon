from django.db import models
from django import forms
from django.contrib.auth.models import User

class Disabled_info(models.Model):
    
    SEX_CHOICES= [
        ('1', 'Kobieta'),
        ('2', 'Mężczyzna')
    ]
    
    
    user= models.ForeignKey(User, null=False, blank = False, on_delete=models.CASCADE, default='')
    age = models.IntegerField()
    sex= models.CharField(max_length=10, choices=SEX_CHOICES, default='green')
    city = models.CharField(max_length=200)
    disability_type = models.CharField(max_length= 300)
    
    
    
    
    def __str__(self):
        return self.switch_name


    class Meta:
        verbose_name = "User_info"
        verbose_name_plural = "Users_info"


