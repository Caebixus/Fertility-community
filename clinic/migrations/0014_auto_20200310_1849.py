# Generated by Django 3.0.3 on 2020-03-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0013_basicclinic_no_waiting_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='clinicName',
            field=models.CharField(max_length=80),
        ),
    ]
