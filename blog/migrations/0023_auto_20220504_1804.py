# Generated by Django 3.2.11 on 2022-05-04 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0086_auto_20220504_1804'),
        ('blog', '0022_auto_20220430_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestclinicarticlecity',
            name='accommodation_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='best_clinic_article_city_accommodation_section', to='clinic.basicclinic'),
        ),
        migrations.AddField(
            model_name='bestclinicarticlecity',
            name='distance_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='best_clinic_article_city_distance_section', to='clinic.basicclinic'),
        ),
        migrations.AddField(
            model_name='bestclinicarticlecity',
            name='google_reviews_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='best_clinic_article_city_reviews_section', to='clinic.basicclinic'),
        ),
        migrations.AddField(
            model_name='bestclinicarticlecity',
            name='packages_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='best_clinic_article_city_packages_section', to='clinic.basicclinic'),
        ),
        migrations.AddField(
            model_name='bestclinicarticlecity',
            name='pricing_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='best_clinic_article_city_pricing_section', to='clinic.basicclinic'),
        ),
    ]