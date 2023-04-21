from django import template
import django_filters
from django_filters import FilterSet
from .models import Machine

register = template.Library()
@register.filter()
def filter(value):
    return f'{value[:-3]}' 

class MachinesFilter(FilterSet):
    modelMachine__name = django_filters.CharFilter(label='Модель', lookup_expr='icontains')
    engine__name = django_filters.CharFilter(label='Двигатель', lookup_expr='icontains')
    transmission__name = django_filters.CharFilter(label='Трансмиссия', lookup_expr='icontains')
    steringAxel__name = django_filters.CharFilter(label='Ведущий мост', lookup_expr='icontains')
    driveAxel__name = django_filters.CharFilter(label='Управляемый мост', lookup_expr='icontains')
   
    class Meta:
        model = Machine
        fields = ['modelMachine__name','engine__name','transmission__name','steringAxel__name','driveAxel__name',]


class ServiceFilter(FilterSet):
    typeOfService__name = django_filters.CharFilter(label='Тип ТО', lookup_expr='icontains')
    machine__factoryNumberMachine = django_filters.CharFilter(label='Заводской номер', lookup_expr='icontains')
    serviceCompany__name = django_filters.CharFilter(label='Сервисная компания', lookup_expr='icontains')
    
   
    class Meta:
        model = Machine
        fields = ['typeOfService__name','machine__factoryNumberMachine','serviceCompany__name',]