from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializerAll, MachineSerializerAny

# Create your views here.


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
