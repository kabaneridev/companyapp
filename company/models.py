from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField
import django_filters

TYPES = (
        ('startup', 'Startup'),
        ('software_house', 'Software House'),
        ('e-commerce', 'E-commerce'),
        ('corporation', 'Corporation'),
    )

CITIES = (
         ('warszawa', 'Warszawa'),
         ('poznan', 'Poznan'),
         ('szczecin', 'Szczecin'),
         ('gdansk', 'Gdansk'),
         ('krakow', 'Krakow'),
         ('wroclaw', 'Wroclaw'),
         ('katowice', 'Katowice'),
         ('gliwice', 'Gliwice')

    )

COMPANY_TECHNOLOGIES = (
        ('php', 'PHP'),
        ('js', 'JavaScript'),
        ('ang', 'Angular'),
        ('java', 'Java'),
        ('ruby', 'Ruby'),
        ('ror', 'Ruby on Rails'),
        ('jee', 'Java EE'),
        ('python', 'Python'),
        ('django' , 'Django'),
    )


class company(models.Model):
    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=15, choices=TYPES)
    workers = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    city = models.CharField(max_length=15,choices=CITIES)
    stack = models.CharField(max_length=15, choices=COMPANY_TECHNOLOGIES)
    company_about = models.TextField(max_length=500, blank=False)   
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.name

    
   
