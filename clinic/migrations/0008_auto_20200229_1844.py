# Generated by Django 3.0.3 on 2020-02-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_remove_basicclinic_clinicenglishlanguage'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='clinicEnglish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='clinicGerman',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='clinicPortuguese',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='clinicRussian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='clinicSpanish',
            field=models.BooleanField(default=False),
        ),
    ]
