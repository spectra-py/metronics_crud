# Generated by Django 4.0.4 on 2022-09-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customusers',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]
