# Generated by Django 3.0.3 on 2020-05-02 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0022_auto_20200502_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicclinic',
            old_name='list_date',
            new_name='ppq_update_is_published_list_date',
        ),
        migrations.RenameField(
            model_name='basicclinic',
            old_name='ppq_is_published_list_date',
            new_name='pro_update_is_published_list_date',
        ),
        migrations.RenameField(
            model_name='basicclinic',
            old_name='pro_is_published_list_date',
            new_name='update_list_date',
        ),
    ]
