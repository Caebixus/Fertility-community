# Generated by Django 3.2.11 on 2022-02-19 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_blog_year'),
        ('coaches', '0016_alter_snippet_snippet_blog_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('snippet_blog_relationship', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('snippet_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaches.coaches')),
            ],
        ),
    ]
