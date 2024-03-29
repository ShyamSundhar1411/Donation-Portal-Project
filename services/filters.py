import django_filters
from django import forms
from django_filters import ChoiceFilter, DateRangeFilter
from .models import Donor,DonorRequest

class DonorFilter(django_filters.FilterSet):
    pin_code = django_filters.CharFilter(lookup_expr='icontains',label = "Pin Code Lookup")
    # show_compatible_types = django_filters.BooleanFilter(field_name = "compatible_types",method = "type_filter",widget=forms.CheckboxInput)
    # def type_filter(self,queryset,blood_type,value):
    #     return queryset.filter(blood_type=value,compatible_types__icontains = value)
    class Meta:
        model = Donor
        fields = ['blood_type','state']

class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = DonorRequest
        fields = ['blood_type','include_compatible_blood']
