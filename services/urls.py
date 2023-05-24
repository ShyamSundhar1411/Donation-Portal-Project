from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('profile/<slug:slug>/',views.profile,name = "profile"),
    path('request/donation/',views.blood_donation_request,name = "request_blood"),
]