# Generated by Django 3.2.11 on 2022-02-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0030_alter_coaches_coach_preferred_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaches',
            name='coach_preferred_languages',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
