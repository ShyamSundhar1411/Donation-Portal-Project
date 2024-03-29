
from .forms import *
from .models import *
from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse_lazy

from django.contrib import messages
from .filters import DonorFilter,RequestFilter
from .aiding_functions import find_compatible_match,is_authorized

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
    filter = DonorFilter(request.GET, queryset=Donor.objects.filter(role = "Donor",user__is_superuser = False).exclude(user = request.user)) 
    checker = request.GET.get("show_compatible_types_check","")
    records = filter.qs
    if checker=="on":
        blood_type = request.GET.get("blood_type","")
        if blood_type == "B +ve" or blood_type == "B -ve":
            print("Hey B +ve")
            blood_type = ";"+blood_type
        extra_data = Donor.objects.filter(compatible_types__icontains = blood_type)
        records = (records | extra_data)
    return render(request, "services/home.html", {'filter': filter,"records":records})


@login_required
def profile(request, slug):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        donor_form = DonorForm(request.POST, request.FILES, instance=request.user.donor)
        if user_form.is_valid() and donor_form.is_valid() :
            donor_form_copy = donor_form.save(commit=False)
            if request.user.donor.role == "Unauthorized":
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

@login_required
def blood_donation_request(request):
    if not request.user.donor.contact:
        messages.info(
            request, "Verify your account by adding Contact Number before proceeding to the portal")
        return redirect("profile", slug=request.user.donor.slug)
    donor = request.user.donor
    existing_request = DonorRequest.objects.filter(donor=donor,request_status="Pending").exists()
    if existing_request:
        messages.info(request,"You already have a request pending")
        return redirect("home")
    if request.method == 'POST':
        donor_request_form = DonorRequestForm(request.POST)
        if donor_request_form.is_valid():
            donor_request_form_copy = donor_request_form.save(commit=False)
            donor_request_form_copy.donor=request.user.donor
            donor_request_form_copy.save()
            messages.success(request, 'Request Created Successfully')
            return redirect('home')
        else:
            messages.error(request,'bad data passed')
            return render(request, 'services/request_blood.html', {'donor_request_form': donor_request_form, 'donor_request_form_errors': donor_request_form.errors})
    else:
        donor_request_form = DonorRequestForm()
        return render(request, 'services/request_blood.html', {'donor_request_form': donor_request_form})

@login_required
def view_request(request):
    if not request.user.donor.contact:
        messages.info(
            request, "Verify your account by adding Contact Number before proceeding to the portal")
        return redirect("profile", slug=request.user.donor.slug)
    filter = RequestFilter(request.GET, queryset=DonorRequest.objects.filter(blood_type=request.user.donor.blood_type)) 
    return render(request, "services/view_requests.html", {'filter': filter})


@login_required
def accept_request(request,slug):
    if not request.user.donor.contact:
        messages.info(
            request, "Verify your account by adding Contact Number before proceeding to the portal")
        return redirect("profile", slug=request.user.donor.slug)
    accepting_donor = request.user.donor
    donor_request=DonorRequest.objects.get(slug = slug)
    donor_approval = DonationApplication.objects.create(donor_request=donor_request,donor = accepting_donor,status = "Pending")
    messages.success(request, 'Thank you for your initiative! Your response has been recorded successfully')
    return redirect('home')
    
@login_required
@user_passes_test(lambda user:is_authorized(user))
def view_all_request_admin(request):
    requests = DonorRequest.objects.all()
    return render(request,"services/view_all_requests.html",{"requests":requests})