# Generated by Django 3.0.3 on 2020-05-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contactwebsite_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactwebsite',
            name='anti_spam_challenge',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
