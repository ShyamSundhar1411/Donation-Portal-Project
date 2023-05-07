from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('profile/<slug:slug>',views.profile,name = "profile"),
    path('profile/request/<slug:slug>',views.request,name = "request"),
]