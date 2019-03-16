from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField
import django_filters

TYPES = (
        ('Startup', 'Startup'),
        ('Software House', 'Software House'),
        ('E-commerce', 'E-commerce'),
        ('Corporation', 'Corporation'),
    )

CITIES = (
         ('Warszawa', 'Warszawa'),
         ('Poznan', 'Poznan'),
         ('Szczecin', 'Szczecin'),
         ('Gdansk', 'Gdansk'),
         ('Krakow', 'Krakow'),
         ('Wroclaw', 'Wroclaw'),
         ('Katowice', 'Katowice'),
         ('Gliwice', 'Gliwice')

    )

COMPANY_TECHNOLOGIES = (
        ('PHP', 'PHP'),
        ('js', 'JavaScript'),
        ('ang', 'Angular'),
        ('java', 'Java'),
        ('ruby', 'Ruby'),
        ('ror', 'Ruby on Rails'),
        ('jee', 'Java EE'),
        ('python', 'Python'),
        ('django' , 'Django'),
    )

STUDENTS = (
		('No', 'No'),
		('Yes', 'Yes')
	)


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)
    students = models.CharField(max_length=3, choices=STUDENTS)
    type = models.CharField(max_length=15, choices=TYPES)
    workers = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    city = models.CharField(max_length=15,choices=CITIES)
    stack = MultiSelectField(choices=COMPANY_TECHNOLOGIES)
    ##stack = models.CharField(max_length=15, choices=COMPANY_TECHNOLOGIES)
    stack_two = models.CharField(max_length=15, choices=COMPANY_TECHNOLOGIES, default='value')
    company_about = models.TextField(max_length=500, blank=False)   
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.name

class AddCompany(models.Model):
    name = models.CharField(max_length=200, blank=False)
    company_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15, blank=True)

    
   
