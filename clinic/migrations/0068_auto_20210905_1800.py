# Generated by Django 3.0.3 on 2021-09-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0067_auto_20210905_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='clinicGoogleReviewsUrl',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
    ]
