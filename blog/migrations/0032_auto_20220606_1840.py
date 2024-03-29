# Generated by Django 3.2.11 on 2022-06-06 18:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_modularbestclinics_link_fertility_clinics'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqblog',
            name='faq_bestclinicarticlecountry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='faq_bestclinicarticlecountry_reverse', to='blog.bestclinicarticlecountry'),
        ),
        migrations.AddField(
            model_name='faqblog',
            name='faq_bestclinicarticlecountry_answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faqblog',
            name='faq_bestclinicarticlecountry_question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
