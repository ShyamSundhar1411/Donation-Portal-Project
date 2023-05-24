from django.contrib import admin
from .models import Donor,DonationApplication,DonorRequest
# Register your models here.
admin.site.register(Donor)
admin.site.register(DonationApplication)
admin.site.register(DonorRequest)