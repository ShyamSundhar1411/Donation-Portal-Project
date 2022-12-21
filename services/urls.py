from django.urls import include,path
from . import views


urlpatterns = [
    path('profile/<slug:slug>',views.profile,name = "profile"),
]