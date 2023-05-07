from django.contrib import admin
from .models import Donor,DonorApproval,DonorRequest
# Register your models here.
admin.site.register(Donor)
admin.site.register(DonorApproval)
admin.site.register(DonorRequest)