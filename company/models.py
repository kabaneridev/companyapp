from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinValueValidator, URLValidator
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

STACK = (
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
STACK_ICONS = (
        ('/static/icons/stack/php.png', 'PHP'),
        ('/static/icons/stack/javascript.png', 'JavaScript'),
    )

POSITIONS = (
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('COO', 'Chief Operating Officer'),
        ('CFO', 'Chief Financial Officer'),
        ('Co-Founder', 'Co-Founder'),
        ('Lead Software Developer', 'Lead Software Developer'),
        ('Software Developer', 'Software Developer'),
        ('Front-end Developer', 'Front-end Developer'),
        ('Back-end Developer', 'Back-end Developer'),
        ('QA Engineer', 'QA Engineer'),
        ('Scrum Master', 'Scrum Master'),
        ('HR Recruiter', 'HR recruiter'),
    )

# object position with relationship many to many to person

class Position(models.Model):
    position = models.CharField(max_length=50, choices=POSITIONS)

    def __str__(self):
        return self.position

# object person relation many to one (many persons to one company)

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField(max_length=500, default=None)
    position = models.ManyToManyField('Position')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

# object company

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)
    students = models.CharField(max_length=3, choices=STUDENTS)
    type = models.CharField(max_length=15, choices=TYPES)
    workers = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    city = models.CharField(max_length=15,choices=CITIES)
    company_about = models.TextField(max_length=500, blank=False)   
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    technologies = models.ManyToManyField('Stack')
    website = models.TextField(max_length=150, blank=True, null=True, validators=[URLValidator()])
    facebook = models.TextField(max_length=150, blank=True, null=True, validators=[URLValidator()])
    instagram = models.TextField(max_length=150, blank=True, null=True, validators=[URLValidator()])
    youtube = models.TextField(max_length=150, blank=True, null=True, validators=[URLValidator()])
    twitter = models.TextField(max_length=150, blank=True, null=True, validators=[URLValidator()])
    linkedin = models.TextField(max_length=150, blank=True, null=True, validators=[URLValidator()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.name

# object stack relation manytomany with Company

class Stack(models.Model):
    name = models.CharField(max_length=30, choices=STACK)
    icon = models.CharField(max_length=80, choices=STACK_ICONS)

    def __str__(self):
        return self.name

