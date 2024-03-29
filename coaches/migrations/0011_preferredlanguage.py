# Generated by Django 3.2.11 on 2022-02-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0010_alter_typejobs_coaches_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferredLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_language', models.CharField(blank=True, max_length=256, null=True)),
                ('coaches_relationship', models.ManyToManyField(blank=True, related_name='languages', to='coaches.Coaches')),
            ],
        ),
    ]
