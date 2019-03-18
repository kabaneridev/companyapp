from django.contrib import admin
from .models import Company, Stack, Person, Position

admin.site.register(Company)
admin.site.register(Stack)
admin.site.register(Person)
admin.site.register(Position)