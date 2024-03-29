# Generated by Django 3.0.3 on 2021-09-04 11:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0060_auto_20210804_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_currency', models.CharField(max_length=10, null=True)),
                ('package1title', models.CharField(blank=True, max_length=30, null=True)),
                ('package1category', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('package1desc', models.TextField(blank=True, max_length=500, null=True)),
                ('package1cost', models.FloatField(blank=True, null=True)),
                ('package2title', models.CharField(blank=True, max_length=30, null=True)),
                ('package2category', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('package2desc', models.TextField(blank=True, max_length=500, null=True)),
                ('package2cost', models.FloatField(blank=True, null=True)),
                ('package3title', models.CharField(blank=True, max_length=30, null=True)),
                ('package3category', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('package3desc', models.TextField(blank=True, max_length=500, null=True)),
                ('package3cost', models.FloatField(blank=True, null=True)),
                ('package4title', models.CharField(blank=True, max_length=30, null=True)),
                ('package4category', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('package4desc', models.TextField(blank=True, max_length=500, null=True)),
                ('package4cost', models.FloatField(blank=True, null=True)),
                ('package5title', models.CharField(blank=True, max_length=30, null=True)),
                ('package5category', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('package5desc', models.TextField(blank=True, max_length=500, null=True)),
                ('package5cost', models.FloatField(blank=True, null=True)),
                ('package6title', models.CharField(blank=True, max_length=30, null=True)),
                ('package6category', models.CharField(choices=[('IVF', 'IVF'), ('Egg Donation', 'Egg Donation'), ('Embryo Donation', 'Embryo Donation')], default='IVF', max_length=40, null=True)),
                ('package6desc', models.TextField(blank=True, max_length=500, null=True)),
                ('package6cost', models.FloatField(blank=True, null=True)),
                ('clinic_pro_promotion_name', models.CharField(blank=True, max_length=80, null=True)),
                ('clinic_pro_promotion_description', models.TextField(blank=True, max_length=800, null=True)),
                ('clinic_pro_promotion_landing_url', models.URLField(blank=True, max_length=500, null=True)),
                ('clinic_staff', ckeditor.fields.RichTextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AcceptedPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_payment', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='clinic_pro_promotion_description',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='clinic_pro_promotion_landing_url',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='clinic_pro_promotion_name',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='clinic_staff',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package1category',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package1cost',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package1desc',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package1title',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package2category',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package2cost',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package2desc',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package2title',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package3category',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package3cost',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package3desc',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package3title',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package4category',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package4cost',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package4desc',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package4title',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package5category',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package5cost',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package5desc',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package5title',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package6category',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package6cost',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package6desc',
        ),
        migrations.RemoveField(
            model_name='basicclinic',
            name='package6title',
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
