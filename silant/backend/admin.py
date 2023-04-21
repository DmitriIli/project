from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin
from .models import *


@admin.register(Parts)
class PartsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ModelMachine)
class ModelMachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(DriveAxel)
class DriveAxelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(SteringAxel)
class SteringAxelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(ServiceCompany)
class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(ClientCompany)
class ClientCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(MaintenanceCompany)
class MaintenanceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(TypeOfService)
class TypeOfServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    # list_display = ('__all__',)
    ...
    


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    ...
    # list_display = ('name',)


@admin.register(Complainte)
class ComplainteAdmin(admin.ModelAdmin):
    ...
    # list_display = ('name',)


@admin.register(ServiceCompanyUser)
class ServiceCompanyUserAdmin(admin.ModelAdmin):
    ...
    # list_display = ('name',)


@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    ...
    # list_display = ('name',)


@admin.register(ManagerUser)
class ManagerUserAdmin(admin.ModelAdmin):
    ...
    # list_display = ('name',)

