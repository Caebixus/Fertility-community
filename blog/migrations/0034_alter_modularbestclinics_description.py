# Generated by Django 3.2.11 on 2022-06-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_alter_modularbestclinics_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modularbestclinics',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
