# Generated by Django 3.0.3 on 2021-10-03 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0077_auto_20211003_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicclinic',
            name='best_article_city_actual_prototype',
            field=models.TextField(blank=True, max_length=3750, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='best_article_city_actual_text',
            field=models.TextField(blank=True, max_length=3750, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='best_article_state_actual_prototype',
            field=models.TextField(blank=True, max_length=3750, null=True),
        ),
        migrations.AlterField(
            model_name='basicclinic',
            name='best_article_state_actual_text',
            field=models.TextField(blank=True, max_length=3750, null=True),
        ),
    ]