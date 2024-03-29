# Generated by Django 3.0.3 on 2020-05-02 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0021_auto_20200325_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='ppq_is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='ppq_is_published_list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='ppq_list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
