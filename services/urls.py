from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('profile/<slug:slug>/',views.profile,name = "profile"),
    path('request/donation/',views.blood_donation_request,name = "request_blood"),
    path('view/request/blood/',views.view_request,name = "view_request"),
    path('view/all/request/',views.view_all_request_admin,name = "view_all_request"),
    path('view/request/<slug:slug>/accept/',views.accept_request,name = "accept_donation_request")
]