# Generated by Django 3.2.11 on 2022-02-19 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_blog_year'),
        ('coaches', '0022_alter_snippetnew_snippet_blog_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippetnew',
            name='snippet_blog_relationship',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
    ]