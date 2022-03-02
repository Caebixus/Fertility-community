# Generated by Django 3.2.11 on 2022-02-17 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_coaches_coach_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_1', models.CharField(default='Fertility Coach', max_length=256)),
                ('type_2', models.CharField(default='Fertility Specialist', max_length=256)),
                ('type_3', models.CharField(default='Reproductive Endocrinologist', max_length=256)),
                ('type_4', models.CharField(default='Andrologist', max_length=256)),
                ('type_5', models.CharField(default='Reproductive Surgeon', max_length=256)),
                ('type_6', models.CharField(default='Reproductive Immunologist', max_length=256)),
                ('type_7', models.CharField(default='Obstetrician', max_length=256)),
                ('type_8', models.CharField(default='Gynecologist', max_length=256)),
                ('base_coach', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='coaches.coaches')),
            ],
        ),
    ]
