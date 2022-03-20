# Generated by Django 3.2.11 on 2022-03-20 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coaches', '0035_auto_20220306_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaches',
            name='coach_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
