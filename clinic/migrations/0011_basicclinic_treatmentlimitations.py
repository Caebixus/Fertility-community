# Generated by Django 3.0.3 on 2020-03-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_auto_20200307_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='treatmentLimitations',
            field=models.TextField(blank=True, max_length=800),
        ),
    ]
