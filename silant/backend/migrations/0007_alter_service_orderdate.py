# Generated by Django 4.2 on 2023-04-20 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_complainte_downtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='orderDate',
            field=models.DateField(default=datetime.date(2023, 4, 20), verbose_name='Дата заказ-наряда'),
        ),
    ]