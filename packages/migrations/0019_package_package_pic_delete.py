# Generated by Django 3.0.3 on 2020-12-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0018_auto_20201201_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_pic_delete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]