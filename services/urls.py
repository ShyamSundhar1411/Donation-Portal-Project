from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('profile/<slug:slug>',views.profile,name = "profile"),
    path('profile/request/<slug:slug>',views.donor_request,name = "request"),
    path('profile/request/views/<slug:slug>',views.request_view,name = "request_view"),
]