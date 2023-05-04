from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import MachineSerializerAll, MachineSerializerAny
from .filters import MachinesFilter, ServiceFilter, MaintFilter
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from backend.serializers import UserSerilazer, LoginRequestSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

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


@api_view(['POST'])
@permission_classes([AllowAny])
def auth_login(request: Request):
    serializer = LoginRequestSerializer(data=request.data)
    if serializer.is_valid():
        authenticated_user = authenticate(**serializer.validated_data)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return Response({'status': 'Success'})
        else:
            return Response({'error': 'Invalid credentials'}, status=403)
    else:
        return Response(serializer.errors, status=400)


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def user(request: Request):
    return Response({
        'data': UserSerilazer(request.user).data
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def auth_logout(request: Request):
    logout(request)
    return Response(status=200)

# def logout(request):
#     try:
#         del request.session['user']
#     except:
#         return redirect('login')
#     return redirect('login')
