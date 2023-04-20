import django_filters
from django_filters import FilterSet
from .models import Machine


class MachinesFilter(FilterSet):
    modelMachine__name = django_filters.CharFilter(label='Модель', lookup_expr='icontains')
    engine__name = django_filters.CharFilter(label='Двигатель', lookup_expr='icontains')
    transmission__name = django_filters.CharFilter(label='Трансмиссия', lookup_expr='icontains')
    steringAxel__name = django_filters.CharFilter(label='Ведущий мост', lookup_expr='icontains')
    driveAxel__name = django_filters.CharFilter(label='Управляемый мост', lookup_expr='icontains')
   
    class Meta:
        model = Machine
        fields = ['modelMachine__name','engine__name','transmission__name','steringAxel__name','driveAxel__name',]