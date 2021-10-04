# Generated by Django 3.0.3 on 2021-10-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0079_auto_20211003_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicclinic',
            name='best_article_city_fcreview_text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='best_article_country_fcreview_text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='basicclinic',
            name='best_article_state_fcreview_text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
