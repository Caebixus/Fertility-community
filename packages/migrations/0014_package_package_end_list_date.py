# Generated by Django 3.0.3 on 2020-10-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0013_auto_20201010_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_end_list_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]