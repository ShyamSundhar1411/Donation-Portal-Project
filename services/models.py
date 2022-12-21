import uuid
from django.db import models
from django.contrib.auth.models import User
from .choices import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length = 100,choices = ROLE_CHOICES,default = "Donor")
    blood_type=models.CharField(max_length=100,choices=BLOOD_CHOICES)
    address = models.TextField(max_length=300)
    last_donated = models.DateField(blank=True,null = True)
    contact = PhoneNumberField(blank=True)
    slug= models.SlugField(max_length=100,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Donor, self).save(*args, **kwargs)
    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Donor.objects.create(user=instance, role="Unauthorized",address=" ")
        instance.donor.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.donor.save()
