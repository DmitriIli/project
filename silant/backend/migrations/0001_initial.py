# Generated by Django 4.2 on 2023-04-10 06:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCompany',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DriveAxel',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('factoryNumberMachine', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='Machine factory number')),
                ('factoryNumberEngine', models.CharField(max_length=64, unique=True, verbose_name='Engine Factory Number')),
                ('factoryNumberTransmission', models.CharField(max_length=64, unique=True, verbose_name='Transmission Factory Number')),
                ('factoryNumberDriveAxel', models.CharField(max_length=64, unique=True, verbose_name='Drive Axel Factory Number')),
                ('factoryNumberSteringAxel', models.CharField(max_length=64, unique=True, verbose_name='Stering Axel Factory Number')),
                ('supplyContract', models.CharField(max_length=64, verbose_name='Contract Number')),
                ('shipingDate', models.DateField(default=datetime.date(2023, 4, 10), verbose_name='Shiping Date')),
                ('receiver', models.CharField(max_length=64, verbose_name='Receiver')),
                ('deliveryAddress', models.CharField(max_length=256, verbose_name='Delivery Address')),
                ('equipment', models.CharField(default='стандартная комплектация', max_length=256, verbose_name='Equipment')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.clientcompany', verbose_name='Client Company')),
                ('driveAxel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.driveaxel', verbose_name='Drive Axel')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.engine', verbose_name='Engine')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceCompany',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ModelMachine',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
            options={
                'verbose_name': 'Model',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Parts',
            },
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SteringAxel',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfService',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompanyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateService', models.DateField(auto_now_add=True)),
                ('operatingTime', models.IntegerField(default=0)),
                ('orderNumber', models.CharField(max_length=64)),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.machine')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany')),
                ('typeOfService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.typeofservice')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='modelMachine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.modelmachine', verbose_name='Model Machine'),
        ),
        migrations.AddField(
            model_name='machine',
            name='serviceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany', verbose_name='Service Company'),
        ),
        migrations.AddField(
            model_name='machine',
            name='steringAxel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.steringaxel', verbose_name='Stering Axel'),
        ),
        migrations.AddField(
            model_name='machine',
            name='transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.transmission', verbose_name='Transmission'),
        ),
        migrations.CreateModel(
            name='Complainte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failureDate', models.DateField(auto_now_add=True)),
                ('operatingTime', models.IntegerField(default=0)),
                ('failureDescription', models.CharField(default='описание', max_length=256)),
                ('spareParts', models.CharField(default='зап.части', max_length=256)),
                ('recoveryDate', models.DateField(auto_now_add=True)),
                ('downTime', models.IntegerField(default=0)),
                ('failurePart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.parts')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.machine')),
                ('maintenanceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.maintenancecompany')),
                ('recoveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.recoverymethod')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany')),
            ],
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.clientcompany')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
