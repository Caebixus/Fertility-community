# Generated by Django 3.0.3 on 2021-10-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0003_authenticateduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticateduser',
            name='random_auth_string',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
