# Generated by Django 3.0.3 on 2020-02-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_basicclinic_clinicown'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='clinicEnglishLanguage',
            field=models.BooleanField(default=False),
        ),
    ]
