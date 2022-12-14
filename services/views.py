from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def home(request):
    return render(request,"services/home.html",)
def profile(request):
    
    return render(request,'services/profile.html',{'form':DonorForm()})
