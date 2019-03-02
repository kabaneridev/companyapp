import django_filters
from .models import company

class CompanyFilter(django_filters.FilterSet):

    class Meta:
        model = company
        fields = ['type', 'city', 'stack']