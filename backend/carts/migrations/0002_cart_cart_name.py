# Generated by Django 4.1.4 on 2022-12-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
