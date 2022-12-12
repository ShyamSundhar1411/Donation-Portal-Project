from django.db import models
from django.contrib.auth.models import User
from .choices import *
# Create your models here.

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length = 100,choices = ROLE_CHOICES,default = "Donor")
    blood_type=models.CharField(max_length=100,choices=BLOOD_CHOICES)
    address = models.TextField(max_length=300)
    last_donated = models.DateField(blank=True,null = True)
    def __str__(self):
        return self.user.username

