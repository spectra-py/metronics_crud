# Generated by Django 4.0.4 on 2022-09-27 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orbit_auth', '0005_customusers_forgot_password_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
