# Generated by Django 3.0.3 on 2021-04-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0049_auto_20210421_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='clinicTrustPilotDomain',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
