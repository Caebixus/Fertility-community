# Generated by Django 3.2.11 on 2022-04-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_faqblog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqblog',
            name='active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
