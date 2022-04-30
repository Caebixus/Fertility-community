# Generated by Django 3.2.11 on 2022-04-30 14:59

import ckeditor.fields
import clinic.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_faqblog_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqblog',
            name='tag',
            field=models.CharField(choices=[('FAQ', 'FAQ')], max_length=40, null=True),
        ),
        migrations.CreateModel(
            name='SimpleBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=150)),
                ('keywords', models.CharField(blank=True, max_length=150, null=True)),
                ('pic_blog', models.ImageField(blank=True, null=True, upload_to='blogPhotos', validators=[clinic.validators.validate_file_size])),
                ('tag', models.CharField(choices=[('IVF-Abroad', 'IVF-Abroad'), ('IVF Packages', 'IVF Packages'), ('IVF Costs', 'IVF Costs'), ('Educational', 'Educational'), ('Informational&Supportive', 'Informational&Supportive'), ('Research', 'Research')], max_length=40, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('minute_read', models.IntegerField(blank=True, null=True)),
                ('year', models.PositiveIntegerField(blank=True, default=2022, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('introduction', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entries_simple_article', to='blog.author')),
            ],
        ),
    ]
