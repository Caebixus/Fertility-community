# Generated by Django 3.0.3 on 2020-05-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0023_auto_20200502_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='query_email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]