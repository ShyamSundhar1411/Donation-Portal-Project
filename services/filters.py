import django_filters
from django_filters import ChoiceFilter, DateRangeFilter
from .models import Donor

class DonorFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(lookup_expr='icontains')
    date_of_birth = DateRangeFilter(label='Last Donated')
    class Meta:
        model = Donor
        fields = ['blood_type']
