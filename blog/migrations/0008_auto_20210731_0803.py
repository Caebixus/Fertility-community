# Generated by Django 3.0.3 on 2021-07-31 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210713_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='last_modified',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
