import django_filters
from django import forms
from django_filters import ChoiceFilter, DateRangeFilter
from .models import Donor

class DonorFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(lookup_expr='icontains',label = "Address Lookup")
    # show_compatible_types = django_filters.BooleanFilter(field_name = "compatible_types",method = "type_filter",widget=forms.CheckboxInput)
    # def type_filter(self,queryset,blood_type,value):
    #     return queryset.filter(blood_type=value,compatible_types__icontains = value)
    class Meta:
        model = Donor
        fields = ['blood_type',]
