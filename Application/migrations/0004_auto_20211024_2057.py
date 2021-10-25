# Generated by Django 3.2.8 on 2021-10-25 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_auto_20211024_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.user')),
            ],
        ),
    ]
