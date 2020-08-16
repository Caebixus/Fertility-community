# Generated by Django 3.0.3 on 2020-08-15 09:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_auto_20200814_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='packagescategory',
            field=models.CharField(choices=[('IVF packages', 'IVF packages'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF packages', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='packages',
            name='packagesdesc',
            field=ckeditor.fields.RichTextField(blank=True, max_length=800, null=True),
        ),
    ]
