# Generated by Django 3.0.3 on 2021-06-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0055_auto_20210530_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='digitalTransparencyIndex',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
