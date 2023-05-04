from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer, CharField
from .models import Machine
from django.contrib.auth.models import User


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


class UserSerilazer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'date_joined']


class LoginRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)
