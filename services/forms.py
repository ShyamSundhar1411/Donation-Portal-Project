from django import forms
from .models import *
from .choices import *
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User

class DonorForm(forms.ModelForm):
    role= forms.CharField(disabled=True)
    contact= PhoneNumberField(required=True)
    compatible_types = forms.ChoiceField(disabled=True,required=False,choices = COMPATBILE_TYPES)
    class Meta:
        model=Donor
        fields=['role','blood_type','address','contact','date_of_birth','compatible_types']

class UserForm(forms.ModelForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']