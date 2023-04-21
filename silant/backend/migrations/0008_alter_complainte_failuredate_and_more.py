# Generated by Django 4.1.5 on 2023-04-21 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_service_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainte',
            name='failureDate',
            field=models.DateField(default=datetime.date(2023, 4, 21), verbose_name='Дата отказа'),
        ),
        migrations.AlterField(
            model_name='complainte',
            name='recoveryDate',
            field=models.DateField(default=datetime.date(2023, 4, 21), verbose_name='Дата восстановления'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='shipingDate',
            field=models.DateField(default=datetime.date(2023, 4, 21), verbose_name='Дата отгрузки'),
        ),
        migrations.AlterField(
            model_name='service',
            name='orderDate',
            field=models.DateField(default=datetime.date(2023, 4, 21), verbose_name='Дата заказ-наряда'),
        ),
    ]
