# Generated by Django 2.0.13 on 2019-03-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20190302_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(choices=[('warszawa', 'Warszawa'), ('poznan', 'Poznan'), ('szczecin', 'Szczecin'), ('gdansk', 'Gdansk'), ('krakow', 'Krakow'), ('wroclaw', 'Wroclaw'), ('katowice', 'Katowice'), ('gliwice', 'Gliwice')], max_length=15),
        ),
        migrations.AlterField(
            model_name='company',
            name='stack',
            field=models.CharField(choices=[('php', 'PHP'), ('js', 'JavaScript'), ('ang', 'Angular'), ('java', 'Java'), ('ruby', 'Ruby'), ('ror', 'Ruby on Rails'), ('jee', 'Java EE'), ('python', 'Python'), ('django', 'Django')], max_length=15),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('startup', 'Startup'), ('software_house', 'Software House'), ('e-commerce', 'E-commerce'), ('corporation', 'Corporation')], max_length=15),
        ),
    ]