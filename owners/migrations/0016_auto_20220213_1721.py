# Generated by Django 3.2.11 on 2022-02-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0015_auto_20220213_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticateduser',
            name='register_as_clinic',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='authenticateduser',
            name='register_as_coach',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
