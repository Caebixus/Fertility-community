# Generated by Django 3.0.3 on 2021-09-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0070_auto_20210908_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='description',
            field=models.TextField(blank=True, max_length=1300, null=True),
        ),
    ]