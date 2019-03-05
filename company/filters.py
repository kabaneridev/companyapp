import django_filters
from .models import Company, COMPANY_TECHNOLOGIES
from django_filters import ChoiceFilter

class CompanyFilter(django_filters.FilterSet):

	class Meta:
		model = Company
		fields = ['type', 'city', 'students']
