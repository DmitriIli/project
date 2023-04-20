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
        ModelMachine, to_field='name', on_delete=models.CASCADE, verbose_name='Модель техники')
    factoryNumberMachine = models.CharField(
        primary_key=True, max_length=64, unique=True, verbose_name='Заводской номер')
    engine = models.ForeignKey(
        Engine, to_field='name', on_delete=models.CASCADE, verbose_name='Модель двигателя')
    factoryNumberEngine = models.CharField(
        max_length=64, unique=True, verbose_name='Заводской номер двигателя')
    transmission = models.ForeignKey(
        Transmission, to_field='name', on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    factoryNumberTransmission = models.CharField(
        max_length=64, unique=True, verbose_name='Заводской номер трансмиссии')
    driveAxel = models.ForeignKey(
        DriveAxel, to_field='name', on_delete=models.CASCADE, verbose_name='Ведущая ось')
    factoryNumberDriveAxel = models.CharField(
        max_length=64, unique=True, verbose_name='Заводской номер ВО')
    steringAxel = models.ForeignKey(
        SteringAxel, to_field='name', on_delete=models.CASCADE, verbose_name='Управляемая ось')
    factoryNumberSteringAxel = models.CharField(
        max_length=64, unique=True, verbose_name='Заводской номер УО')
    supplyContract = models.CharField(
        max_length=64, verbose_name='Договор поставки')
    shipingDate = models.DateField(
        default=date.today(), verbose_name='Дата отгрузки')
    receiver = models.CharField(max_length=64, verbose_name='Получатель')
    deliveryAddress = models.CharField(
        max_length=256, verbose_name='Адрес доставки')
    equipment = models.CharField(
        max_length=256,  default='стандартная комплектация', verbose_name='Комплектация')
    client = models.ForeignKey(
        ClientCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Компания-клиент')
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Сервисная компания')

    class Meta:
        ordering = ['shipingDate']


class Service(models.Model):
    typeOfService = models.ForeignKey(
        TypeOfService, to_field='name', on_delete=models.CASCADE, verbose_name='Тип сервиса')
    dateService = models.DateField(auto_now_add=True, verbose_name='Дата')
    operatingTime = models.IntegerField(
        default=0, verbose_name='Наработка')
    orderNumber = models.CharField(
        max_length=64, verbose_name='№ Заказ-наряд')
    orderDate = models.DateField(
        auto_now_add=True, verbose_name='Дата заказ-наряда')
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Сервисная компания')
    machine = models.ForeignKey(
        Machine, to_field='factoryNumberMachine', on_delete=models.CASCADE, verbose_name='Машина')
    
    
    class Meta:
        ordering = ['dateService']


class Complainte(models.Model):
    machine = models.ForeignKey(
        Machine, to_field='factoryNumberMachine', on_delete=models.CASCADE, verbose_name='Машина')
    failureDate = models.DateField(
        auto_now_add=True, verbose_name='Дата отказа')
    operatingTime = models.IntegerField(
        default=0, verbose_name='Наработка')
    failurePart = models.ForeignKey(
        Parts, to_field='name', on_delete=models.CASCADE, verbose_name='Узел отказа')
    failureDescription = models.CharField(
        max_length=256, default='описание', verbose_name='Описание отказа')
    recoveryMethod = models.ForeignKey(
        RecoveryMethod, to_field='name', on_delete=models.CASCADE, verbose_name='Способ восстановления')
    spareParts = models.CharField(
        default='зап.части', max_length=256, verbose_name='Запасные части')
    recoveryDate = models.DateField(
        auto_now_add=True, verbose_name='Дата восстановления')
    downTime = models.IntegerField(default=0, verbose_name='Время простоя')
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Сервисная компания')
    maintenanceCompany = models.ForeignKey(
        MaintenanceCompany, to_field='name', on_delete=models.CASCADE, verbose_name='Компания, проводившая ТО')

    class Meta:
        ordering = ['downTime']
