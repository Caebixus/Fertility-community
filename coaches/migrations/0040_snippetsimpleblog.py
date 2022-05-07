# Generated by Django 3.2.11 on 2022-05-07 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_rename_slug_simpleblog_simple_slug'),
        ('coaches', '0039_coaches_blog_faq_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetSimpleBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('wait for review', 'wait for review'), ('is published', 'is published'), ('is not approved', 'is not approved')], default='wait for review', max_length=40, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_simple_blog', to='blog.simpleblog')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippet_simple_blog_owner', to='coaches.coaches')),
            ],
        ),
    ]
