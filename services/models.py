import uuid
from django.db import models
from django.contrib.auth.models import User
from .choices import *
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length = 100,choices = ROLE_CHOICES,default = "Donor")
    blood_type=models.CharField(max_length=100,choices=BLOOD_CHOICES)
    house_no = models.CharField(max_length=300,null = True,help_text = "House No/House Name/Street Name")
    state = models.CharField(choices=State_Choices,max_length=255,null = True)
    pin_code = models.CharField(max_length = 500,validators=[RegexValidator("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",message = "Enter a Valid PIN Code")],null = True)
    date_of_birth= models.DateField(blank=True,null=True)
    compatible_types = models.CharField(max_length=500,null=True,choices=COMPATIBLE_TYPES,blank=True)
    contact = PhoneNumberField(blank=True)
    slug= models.SlugField(max_length=100,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Donor, self).save(*args, **kwargs)
    def __str__(self):
        return self.user.username
    @property
    def display_address(self):
        my_address = """{},{}
            {}
        """.format(self.house_no,self.state,self.pin_code)
        return my_address

class DonorRequest(models.Model):
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=300,help_text="Hospital Location")
    blood_type=models.CharField(max_length=100,choices=BLOOD_CHOICES)

class DonorApproval(models.Model):
    donor_request=models.ForeignKey(DonorRequest,on_delete=models.CASCADE)
    Donation_status=models.CharField(max_length = 100,choices = APPROVAL_STATUS,default = "Pending")
    date_approved = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Donor.objects.create(user=instance, role="Unauthorized")
        instance.donor.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.donor.save()
