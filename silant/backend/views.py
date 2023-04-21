from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import MachineSerializerAll, MachineSerializerAny
from .filters import MachinesFilter, ServiceFilter, MaintFilter

# Create your views here.


def getlist(request):
    context, data, titles = {}, [], []
    user = request.user

    if not user.is_authenticated:
        data = Machine.objects.all().values('modelMachine', 'factoryNumberMachine', 'engine', 'factoryNumberEngine', 'transmission',
                                            'factoryNumberTransmission', 'driveAxel', 'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')

    elif user.groups.filter(name='Client').count():
        data = Machine.objects.filter(
            client__clientuser__user=user).values()

    elif user.groups.filter(name='ServiceCompany').count():
        data = Machine.objects.filter(
            serviceCompany__servicecompanyuser__user=user).values()

    elif user.groups.filter(name='Manager').count():
        data = Machine.objects.all().values()

    else:
        print(f'root')

    ls = [item for item in data[0].keys()]

    titles = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]

    f = MachinesFilter(request.GET, queryset=data)

    context = {'data': data, 'titles': titles, 'filter': f}

    return render(request, template_name='frontend/machines.html', context=context)


def machine(request, item):
    context, data, titles, titlesCompl = {}, [], [], []
    data = Service.objects.filter(machine=item).values()
    ls = [item for item in data[0].keys()]
    titles = [Service._meta.get_field(
        f'{name}').verbose_name for name in ls]
    fService = ServiceFilter(request.GET, queryset=data)

    maint = Complainte.objects.filter(machine=item).values()
    print(maint)
    lsd = [item for item in maint[0].keys()]
    titlesC = [Complainte._meta.get_field(
        f'{name}').verbose_name for name in lsd]

    fMaint = MaintFilter(request.GET, queryset=maint)
    context = {'data': data, 'titles': titles, 'filterService': fService,
               'maint': maint, 'titlesC': titlesC, 'filterMaint': fMaint}
    return render(request, template_name='frontend/machine_detail.html', context=context)


def catalog(request, param):
    context, data, titles = {}, [], []
    ls = param.split('&')
    if ls[0] == "engine":
        data = Engine.objects.filter(name=ls[1]).values()
    if ls[0] == "transmission":
        data = Transmission.objects.filter(name=ls[1]).values()
    if ls[0] == "driveAxel":
        data = DriveAxel.objects.filter(name=ls[1]).values()
    if ls[0] == "steringAxel":
        data = SteringAxel.objects.filter(name=ls[1]).values()
    if ls[0] == "serviceCompany":
        data = ServiceCompany.objects.filter(name=ls[1]).values()
    if ls[0] == "typeOfService":
        data = TypeOfService.objects.filter(name=ls[1]).values()
    context = {'data': list(data)}
    return render(request, template_name='frontend/catalog.html', context=context)
