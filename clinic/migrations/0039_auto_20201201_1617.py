# Generated by Django 3.0.3 on 2020-12-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0038_auto_20201125_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='clinic_pro_promotion_landing_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='clinic_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='contact_url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='egg_donor_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='egg_sharing_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='sperm_donor_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]