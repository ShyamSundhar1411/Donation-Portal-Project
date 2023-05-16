from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('profile/<slug:slug>',views.profile,name = "profile"),
    path('profile/request/<slug:slug>',views.donor_request,name = "request_blood"),
    path('profile/request/views/<slug:slug>',views.view_request,name = "view_request"),
    path('profile/request/views/accept/<slug:slug>',views.accept_request,name = "accept_request"),
]