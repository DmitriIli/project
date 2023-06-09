# Generated by Django 4.2 on 2023-04-16 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_complainte_options_alter_machine_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainte',
            name='downTime',
            field=models.IntegerField(default=0, verbose_name='Down Time'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='failureDate',
            field=models.DateField(auto_now_add=True, verbose_name='Failure Data'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='failureDescription',
            field=models.CharField(default='описание', max_length=256, verbose_name='Descripton'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='failurePart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.parts', verbose_name='Failure part'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.machine', verbose_name='Machines'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='maintenanceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.maintenancecompany', verbose_name='Maintenance Company'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='operatingTime',
            field=models.IntegerField(default=0, verbose_name='Operating Time'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='recoveryDate',
            field=models.DateField(auto_now_add=True, verbose_name='recovery Date'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='recoveryMethod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.recoverymethod', verbose_name='Recovery Method'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='serviceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany', verbose_name='Servce Company'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='spareParts',
            field=models.CharField(default='зап.части', max_length=256, verbose_name='Spare Parts'),
        ),
        migrations.AlterField(
            model_name='service',
            name='dateService',
            field=models.DateField(auto_now_add=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='service',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.machine', verbose_name='Machines'),
        ),
        migrations.AlterField(
            model_name='service',
            name='operatingTime',
            field=models.IntegerField(default=0, verbose_name='Operating Time'),
        ),
        migrations.AlterField(
            model_name='service',
            name='orderDate',
            field=models.DateField(auto_now_add=True, verbose_name="Order's Data"),
        ),
        migrations.AlterField(
            model_name='service',
            name='orderNumber',
            field=models.CharField(max_length=64, verbose_name="Order's Number"),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany', verbose_name='Service Company'),
        ),
        migrations.AlterField(
            model_name='service',
            name='typeOfService',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.typeofservice', verbose_name='Type of Service'),
        ),
    ]
