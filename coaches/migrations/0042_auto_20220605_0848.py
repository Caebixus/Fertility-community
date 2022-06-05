# Generated by Django 3.2.11 on 2022-06-05 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20220605_0848'),
        ('coaches', '0041_coaches_coach_is_claimed'),
    ]

    operations = [
        migrations.AddField(
            model_name='coaches',
            name='blog_modular_best_clinics_review',
            field=models.ManyToManyField(blank=True, related_name='blog_modular_best_clinics_review_reviewed_by', to='blog.ModularBestClinics'),
        ),
        migrations.AddField(
            model_name='coaches',
            name='blog_simple_review',
            field=models.ManyToManyField(blank=True, related_name='blog_simple_reviewed_by', to='blog.SimpleBlog'),
        ),
        migrations.CreateModel(
            name='SnippetModularBestClinicsBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('wait for review', 'wait for review'), ('is published', 'is published'), ('is not approved', 'is not approved')], default='wait for review', max_length=40, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_modular_best_clinics_blog', to='blog.modularbestclinics')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippet_modular_best_clinics_blog_owner', to='coaches.coaches')),
            ],
        ),
    ]