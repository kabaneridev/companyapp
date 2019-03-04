import django_filters
from .models import Company
from django_filters import ChoiceFilter

class CompanyFilter(django_filters.FilterSet):
	class Meta:
		model = Company
		fields = ['type', 'city', 'stack']