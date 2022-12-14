from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField

class DonorForm(forms.ModelForm):
    role= forms.CharField(disabled=True)
    contact= PhoneNumberField(required=True)
    class meta:
        model=Donor
        fields=['role','blood_type','address','last_donated','contact']

