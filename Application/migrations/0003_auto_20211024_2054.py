# Generated by Django 3.2.8 on 2021-10-25 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_auto_20211024_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='lastname',
        ),
    ]
