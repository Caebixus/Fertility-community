# Generated by Django 3.2.11 on 2022-06-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_rename_slug_modularbestclinics_modular_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='modularbestclinics',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='modularbestclinics',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='modularbestclinics',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
