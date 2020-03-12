# Generated by Django 3.0.3 on 2020-03-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0015_basicclinic_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='clinicTitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='description',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='treatmentLimitations',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
    ]