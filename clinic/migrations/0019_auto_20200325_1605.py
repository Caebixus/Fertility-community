# Generated by Django 3.0.3 on 2020-03-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0018_auto_20200325_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='package1desc',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]