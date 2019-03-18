# Generated by Django 2.0.13 on 2019-03-18 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0024_auto_20190318_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='youtube',
            field=models.TextField(blank=True, max_length=150, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]