# Generated by Django 3.0.3 on 2021-07-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210408_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.CharField(choices=[('IVF-Abroad', 'IVF-Abroad'), ('IVF Packages', 'IVF Packages'), ('IVF Costs', 'IVF Costs'), ('Educational', 'Educational'), ('Research', 'Research')], max_length=40, null=True),
        ),
    ]
