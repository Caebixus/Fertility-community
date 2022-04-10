# Generated by Django 3.2.11 on 2022-03-06 08:34

import clinic.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0033_auto_20220305_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaches',
            name='coach_profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='fertility_coach', validators=[clinic.validators.validate_file_size]),
        ),
    ]