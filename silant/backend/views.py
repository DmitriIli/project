from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializerAll, MachineSerializerAny

# Create your views here.


@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        try:
            data = Machine.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializers = MachineSerializerAll(data, many=True)
        print(request.user)
        return (Response({'data': serializers.data}, status=status.HTTP_200_OK))


@api_view(['GET'])
def index(request):

    context = {}
    context_json = ''

    if request.method == 'GET':
        try:
            if not request.user.is_authenticated:
                context = Machine.objects.all().values('modelMachine', 'factoryNumberMachine',
                                                       'engine', 'factoryNumberEngine', 'transmission',
                                                       'factoryNumberTransmission', 'driveAxel',
                                                       'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')
                context_json = MachineSerializerAny(context, many=True)

            else:
                context = Machine.objects.all().values()
                context_json = MachineSerializerAll(context, many=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Model._meta.get_field('<field name>').verbose_name

    keys = context[0].keys()
    ls = [item for item in keys]

    verboseNames = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]

    return Response({'context': context_json, 'verboseNames': verboseNames},status=status.HTTP_200_OK)
