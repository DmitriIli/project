from rest_framework import serializers
from .models import Machine


class MachineSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'


class MachineSerializerAny(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('modelMachine', 'factoryNumberMachine',
                  'engine', 'factoryNumberEngine', 'transmission',
                  'factoryNumberTransmission', 'driveAxel',
                  'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')
