# Generated by Django 3.2.11 on 2022-03-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0036_alter_coaches_coach_user'),
        ('clinic', '0084_basicclinic_experts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='experts',
            field=models.ManyToManyField(blank=True, related_name='experts_from_clinic', to='coaches.Coaches'),
        ),
    ]