# Generated by Django 4.0.4 on 2022-06-30 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0005_restaurant_created_restaurant_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='created',
            new_name='timestamp',
        ),
    ]