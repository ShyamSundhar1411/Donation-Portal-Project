from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Donor
from django.contrib import messages
from .filters import DonorFilter
from .aiding_functions import find_compatible_match
# Create your views here.


def landing_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request,"services/landing_page.html",{'donors':Donor.objects.all()})

@login_required
def home(request):
    if not request.user.donor.contact:
        messages.info(
            request, "Verify your account by adding Contact Number before proceeding to the portal")
        return redirect("profile", slug=request.user.donor.slug)
    filter = DonorFilter(request.GET, queryset=Donor.objects.all()) 
    checker = request.GET.get("show_compatible_types_check","")
    records = filter.qs
    if checker=="on":
        blood_type = request.GET.get("blood_type","")
        print(checker)
        extra_data = Donor.objects.filter(compatible_types__icontains = blood_type)
        records = (records | extra_data)
    return render(request, "services/home.html", {'filter': filter,"records":records})


@login_required
def profile(request, slug):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        donor_form = DonorForm(
            request.POST, request.FILES, instance=request.user.donor)
        if user_form.is_valid() and donor_form.is_valid() :
            donor_form_copy = donor_form.save(commit=False)
            donor_form_copy.role='Donor'
            donor_form_copy.compatible_types = find_compatible_match(donor_form.cleaned_data['blood_type'])
            user_form.save()
            donor_form_copy.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile', slug=request.user.donor.slug)
        else:
            messages.error(request,'bad data passed')
            return render(request, 'services/profile.html', {'user_form': user_form, 'donor_form': donor_form, 'user_form_errors': user_form.errors, 'donor_form_errors': donor_form.errors})
    else:
        user_form = UserForm(instance=request.user)
        donor_form = DonorForm(instance=request.user.donor)
        return render(request, 'services/profile.html', {'user_form': user_form, 'donor_form': donor_form})

