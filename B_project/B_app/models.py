
from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_info = models.CharField(max_length=200)
    employee_size = models.IntegerField()
    investor_type = models.CharField(max_length=200)
    contact_mail = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    investment_stage = models.CharField(max_length=200)
    company_type = models.CharField(max_length=200)
    
    
    # Add any other fields you want here
