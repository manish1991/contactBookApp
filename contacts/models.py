from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User	
from django.core.validators import RegexValidator

class Contact(models.Model):
    firstName = models.CharField(max_length=25,blank=True)
    lastName = models.CharField(max_length=25,blank=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{6,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15,validators=[phone_regex], blank=True)
    created_by = models.ForeignKey(User, verbose_name='contact_created_by') 
    date_created = models.DateField(verbose_name="Created on date", auto_now_add="True")