# Generated by Django 4.0.4 on 2022-06-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0007_alter_restaurant_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
