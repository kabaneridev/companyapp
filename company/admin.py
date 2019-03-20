from django.contrib import admin
from .models import Company, Stack, Person, Position, Job, Emp_type

admin.site.register(Company)
admin.site.register(Stack)
admin.site.register(Person)
admin.site.register(Position)
admin.site.register(Job)
admin.site.register(Emp_type)