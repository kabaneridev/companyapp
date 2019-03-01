from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField


class company(models.Model):
    company_name = models.CharField(max_length=100, blank=False)
    COMPANY_TYPES = (
        ('star', 'Startup'),
        ('sh', 'Software House'),
        ('ecom', 'E-commerce'),
        ('corp', 'Corporation'),
        )
    company_types = models.CharField(max_length=4, choices=COMPANY_TYPES)
    company_workers = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    city = models.CharField(max_length=100, blank=False)
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
    company_technologies = MultiSelectField(max_length=25, choices=COMPANY_TECHNOLOGIES, min_choices=1)
    company_about = models.TextField(max_length=500, blank=False)    
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.company_name
