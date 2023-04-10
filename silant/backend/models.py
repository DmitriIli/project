from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


def getOperatingTime():
    ...


class ServiceCompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(
        'ServiceCompany', to_field='name', on_delete=models.CASCADE)


class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clientCompany = models.ForeignKey(
        'ClientCompany', to_field='name', on_delete=models.CASCADE)


class ManagerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parts(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)

    class Meta:
        verbose_name = "Parts"

    def __str__(self) -> str:
        return self.name


class ModelMachine(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    class Meta:
        verbose_name = "Model"

    def __str__(self) -> str:
        return self.name


class Engine(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class Transmission(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class DriveAxel(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class SteringAxel(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class ServiceCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class MaintenanceCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class ClientCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class TypeOfService(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class RecoveryMethod(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)

    def __str__(self) -> str:
        return self.name


class Machine(models.Model):
    modelMachine = models.ForeignKey(
        ModelMachine, to_field='name', on_delete=models.CASCADE, verbose_name='Model Machine')
    factoryNumberMachine = models.CharField(
        primary_key=True, max_length=64, unique=True, verbose_name='Machine factory number')
    engine = models.ForeignKey(
        Engine, to_field='name', on_delete=models.CASCADE, verbose_name='Engine')
    factoryNumberEngine = models.CharField(
        max_length=64, unique=True, verbose_name='Engine Factory Number')
    transmission = models.ForeignKey(
        Transmission, to_field='name', on_delete=models.CASCADE, verbose_name='Transmission')
    factoryNumberTransmission = models.CharField(
        max_length=64, unique=True, verbose_name='Transmission Factory Number')
    driveAxel = models.ForeignKey(
        DriveAxel, to_field='name', on_delete=models.CASCADE, verbose_name='Drive Axel')
    factoryNumberDriveAxel = models.CharField(
        max_length=64, unique=True, verbose_name='Drive Axel Factory Number')
    steringAxel = models.ForeignKey(
        SteringAxel, to_field='name', on_delete=models.CASCADE, verbose_name='Stering Axel')
    factoryNumberSteringAxel = models.CharField(
        max_length=64, unique=True, verbose_name='Stering Axel Factory Number')
    supplyContract = models.CharField(
        max_length=64, verbose_name='Contract Number')
    shipingDate = models.DateField(
        default=date.today(), verbose_name='Shiping Date')
    receiver = models.CharField(max_length=64, verbose_name='Receiver')
    deliveryAddress = models.CharField(
        max_length=256, verbose_name='Delivery Address')
    equipment = models.CharField(
        max_length=256,  default='стандартная комплектация', verbose_name='Equipment')
    client = models.ForeignKey(
        ClientCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Client Company')
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Service Company')


class Service(models.Model):
    typeOfService = models.ForeignKey(
        TypeOfService, to_field='name', on_delete=models.CASCADE)
    dateService = models.DateField(auto_now_add=True)
    operatingTime = models.IntegerField(default=0)
    orderNumber = models.CharField(max_length=64)
    orderDate = models.DateField(auto_now_add=True)
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE)
    machine = models.ForeignKey(
        Machine, to_field='factoryNumberMachine', on_delete=models.CASCADE)


class Complainte(models.Model):
    machine = models.ForeignKey(
        Machine, to_field='factoryNumberMachine', on_delete=models.CASCADE)
    failureDate = models.DateField(auto_now_add=True)
    operatingTime = models.IntegerField(default=0)
    failurePart = models.ForeignKey(
        Parts, to_field='name', on_delete=models.CASCADE)
    failureDescription = models.CharField(max_length=256, default='описание')
    recoveryMethod = models.ForeignKey(
        RecoveryMethod, to_field='name', on_delete=models.CASCADE)
    spareParts = models.CharField(default='зап.части', max_length=256)
    recoveryDate = models.DateField(auto_now_add=True)
    downTime = models.IntegerField(default=0)
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE)
    maintenanceCompany = models.ForeignKey(
        MaintenanceCompany, to_field='name', on_delete=models.CASCADE)