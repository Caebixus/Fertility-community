# Generated by Django 3.0.3 on 2021-04-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0048_auto_20210421_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='clinicGoogleReviews',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
