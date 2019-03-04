# Generated by Django 2.0.13 on 2019-03-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20190302_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='stack_two',
            field=models.CharField(choices=[('php', 'PHP'), ('js', 'JavaScript'), ('ang', 'Angular'), ('java', 'Java'), ('ruby', 'Ruby'), ('ror', 'Ruby on Rails'), ('jee', 'Java EE'), ('python', 'Python'), ('django', 'Django')], default='value', max_length=15),
        ),
        migrations.AlterField(
            model_name='company',
            name='stack',
            field=models.CharField(choices=[('php', 'PHP'), ('js', 'JavaScript'), ('ang', 'Angular'), ('java', 'Java'), ('ruby', 'Ruby'), ('ror', 'Ruby on Rails'), ('jee', 'Java EE'), ('python', 'Python'), ('django', 'Django')], max_length=15),
        ),
    ]