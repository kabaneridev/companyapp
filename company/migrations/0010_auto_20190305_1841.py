# Generated by Django 2.0.13 on 2019-03-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20190305_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
