# Generated by Django 4.1.4 on 2022-12-21 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_cart_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_name',
        ),
    ]
