from __future__ import unicode_literals

from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length = 30)
    org_name = models.CharField(max_length = 30, blank=True)
    description =  models.CharField(max_length = 140)
    location = models.CharField(max_length = 60)
    time = models.DateTimeField('event Time')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.DateTimeField()
    
class user(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    IP_adress = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)