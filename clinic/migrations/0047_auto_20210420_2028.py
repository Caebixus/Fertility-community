# Generated by Django 3.0.3 on 2021-04-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0046_auto_20210420_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='clinicLiveChatChoice',
            field=models.CharField(blank=True, choices=[('Chatra', 'Chatra'), ('Livechat', 'Livechat'), ('Olark', 'Olark'), ('Tidio', 'Tidio')], max_length=40, null=True),
        ),
    ]
