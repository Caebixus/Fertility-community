# Generated by Django 3.0.3 on 2021-09-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0064_auto_20210904_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='accepted_currency_type',
            field=models.ManyToManyField(blank=True, to='clinic.AcceptedCurrency'),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='accepted_payment_type',
            field=models.ManyToManyField(blank=True, to='clinic.AcceptedPayment'),
        ),
    ]
