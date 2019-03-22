# Generated by Django 2.0.13 on 2019-03-22 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190322_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, choices=[('Warszawa', 'Warszawa'), ('Poznan', 'Poznan'), ('Szczecin', 'Szczecin'), ('Gdansk', 'Gdansk'), ('Krakow', 'Krakow'), ('Wroclaw', 'Wroclaw'), ('Katowice', 'Katowice'), ('Gliwice', 'Gliwice')], max_length=15),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_about',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='company',
            name='students',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(blank=True, choices=[('Startup', 'Startup'), ('Software House', 'Software House'), ('E-commerce', 'E-commerce'), ('Corporation', 'Corporation')], max_length=15),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
        ),
    ]