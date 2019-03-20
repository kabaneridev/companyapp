# Generated by Django 2.0.13 on 2019-03-20 12:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0027_company_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('B2B', 'B2B'), ('Pernament', 'Pernament')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=10)),
                ('min_salary', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('max_salary', models.IntegerField(default=None)),
                ('description', models.TextField()),
                ('clausule', models.TextField()),
                ('city', models.CharField(choices=[('Warszawa', 'Warszawa'), ('Poznan', 'Poznan'), ('Szczecin', 'Szczecin'), ('Gdansk', 'Gdansk'), ('Krakow', 'Krakow'), ('Wroclaw', 'Wroclaw'), ('Katowice', 'Katowice'), ('Gliwice', 'Gliwice')], default=None, max_length=20)),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('emp_type', models.ManyToManyField(to='company.Emp_type')),
                ('stack', models.ManyToManyField(to='company.Stack')),
            ],
        ),
    ]