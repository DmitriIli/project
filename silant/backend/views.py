from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import MachineSerializerAll, MachineSerializerAny
from .filters import MachinesFilter, ServiceFilter

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
    context, data, titles = {}, [], []
    data = Service.objects.filter(machine=item).values()
    ls = [item for item in data[0].keys()]
    titles = [Service._meta.get_field(
        f'{name}').verbose_name for name in ls]
    f = ServiceFilter(request.GET, queryset=data)
    context = {'data': data, 'titles': titles, 'filter': f}
    return render(request, template_name='frontend/machine_detail.html', context=context)


def catalog(request, param):
    context, data, titles = {}, [], []
    ls = param.split('&')
    match ls[0]:
        case "engine":
            data = Engine.objects.filter(name=ls[1]).values()
        case _:
            data = []
    
    print(data)
    return render(request, template_name='frontend/catalog.html')


@api_view(['GET'])
def index(request):

    if request.method == 'GET':
        try:
            data = Machine.objects.all()
            if request.user.is_authenticated:

                data_json = MachineSerializerAll(data, many=True)
            else:

                data_json = MachineSerializerAny(data, many=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Model._meta.get_field('<field name>').verbose_name

    ls = [item for item in data_json.data[0].keys()]

    verboseNames = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]

    return Response({'context': data_json.data, 'verboseNames': verboseNames}, status=status.HTTP_200_OK)
