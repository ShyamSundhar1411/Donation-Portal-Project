from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('profile/<slug:slug>/',views.profile,name = "profile"),
    path('request/<slug:slug>/',views.donor_request,name = "request_blood"),
    path('request/views/<slug:slug>/',views.view_request,name = "view_request"),
    path('request/views/accept/<slug:slug>/',views.accept_request,name = "accept_request"),
    path('request/views/all/admin/',views.view_all_request_admin,name = "view_all_requests")
]