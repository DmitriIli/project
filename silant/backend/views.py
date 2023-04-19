from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializerAll, MachineSerializerAny

# Create your views here.


def getlist(request):
    context, data, titles = [], [], []
    user = request.user

    if not user.is_authenticated:
        data = list(Machine.objects.all().values('modelMachine', 'factoryNumberMachine', 'engine', 'factoryNumberEngine', 'transmission',
                                                 'factoryNumberTransmission', 'driveAxel', 'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel'))
        print('not user')
    elif user.groups.filter(name='Client').count():
        data = list(Machine.objects.filter(
            client__clientuser__user=user).values())

    elif user.groups.filter(name='ServiceCompany').count():
        data = list(Machine.objects.filter(
            serviceCompany__servicecompanyuser__user=user).values())

    elif user.groups.filter(name='Manager').count():
        data = list(Machine.objects.all().values())

    else:
        print(f'root')

    ls = [item for item in data[0].keys()]

    titles = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]

    context = {'data': data, 'titles': titles}

    return render(request, template_name='frontend/machines.html', context=context)


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
