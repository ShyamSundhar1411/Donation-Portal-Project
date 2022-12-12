from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.user.donor.role == "Admin":
        return render(request,"services/home.html",)
    else:
        return redirect("profile")
def profile(request):
    return render(request,'services/profile.html')