# Generated by Django 3.0.3 on 2020-11-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0016_auto_20201028_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_pic',
            field=models.ImageField(blank=True, null=True, upload_to='ownerPhotos'),
        ),
    ]
