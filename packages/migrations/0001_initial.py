# Generated by Django 3.0.3 on 2020-06-17 13:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0028_auto_20200518_1633'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagestitle', models.CharField(blank=True, max_length=30, null=True)),
                ('packagescategory', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('packagesdesc', ckeditor.fields.RichTextField(blank=True, max_length=400, null=True)),
                ('packagescost', models.FloatField(blank=True, null=True)),
                ('packageslimitnumber', models.PositiveIntegerField(blank=True, default='0', null=True)),
                ('packageClinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.BasicClinic')),
                ('packageOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
