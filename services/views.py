from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Donor
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "services/home.html")


@login_required
def profile(request, slug):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DonorForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile', slug=request.user.profile.slug)
        else:
            return render(request, 'services/profile.html', {'user_form': user_form, 'profile_form': profile_form, 'user_form_errors': user_form.errors, 'profile_form_errors': profile_form.errors})
    else:
        user_form = UserForm(instance=request.user)
        profile_form = DonorForm(instance=request.user.profile)
        return render(request, 'services/profile.html', {'user_form': user_form, 'profile_form': profile_form})

