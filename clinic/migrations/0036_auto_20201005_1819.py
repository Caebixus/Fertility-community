# Generated by Django 3.0.3 on 2020-10-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0035_basicclinic_packagecliniccounternumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='packageClinicCounterNumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
