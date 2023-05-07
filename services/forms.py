from django import forms
from .models import *
from .choices import *
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User

class DonorForm(forms.ModelForm):
    role = forms.CharField(disabled=True)
    contact = PhoneNumberField(required=True,help_text = "Indicate the country code in front of the number if it's not an Indian number.")
    date_of_birth = forms.DateField(required=True)
    class Meta:
        model=Donor
        fields=['role','blood_type','house_no','state','pin_code','contact','date_of_birth']

class UserForm(forms.ModelForm):
    email = forms.EmailField(disabled= True)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class DonorRequestForm(forms.ModelForm):
    class Meta:
        model = DonorRequest
        fields = ['location','blood_type']
