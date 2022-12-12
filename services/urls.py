from django.urls import include,path
from . import views


urlpatterns = [
    path('profile',views.profile,name = "profile"),
]