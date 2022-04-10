# Generated by Django 3.2.11 on 2022-02-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_alter_coaches_coach_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coaches',
            old_name='coach_prefered_client_city',
            new_name='coach_category',
        ),
        migrations.RenameField(
            model_name='coaches',
            old_name='coach_prefered_client_country',
            new_name='coach_preferred_client_city',
        ),
        migrations.RenameField(
            model_name='coaches',
            old_name='coach_prefered_languages',
            new_name='coach_preferred_client_country',
        ),
        migrations.AddField(
            model_name='coaches',
            name='coach_preferred_languages',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='coaches',
            name='coach_full_name',
            field=models.CharField(max_length=40),
        ),
    ]