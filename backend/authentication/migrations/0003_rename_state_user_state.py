# Generated by Django 4.1.3 on 2022-12-08 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_state_user_city_user_street_user_zip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='State',
            new_name='state',
        ),
    ]
