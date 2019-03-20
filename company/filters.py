import django_filters
from .models import Company, Job
from django_filters import ChoiceFilter

class CompanyFilter(django_filters.FilterSet):

	class Meta:
		model = Company
		fields = ['type', 'city', 'students']

	def __init__(self, *args, **kwargs):
		super(CompanyFilter, self).__init__(*args, **kwargs)
		self.filters['type'].extra.update(
			{'empty_label': 'All'})
		self.filters['city'].extra.update(
			{'empty_label': 'All'})
		self.filters['students'].extra.update(
			{'empty_label': 'All'})

# job filter
class JobFilter(django_filters.FilterSet):
	class Meta:
		model = Job
		fields = ['city', 'stack', 'level', 'min_salary', 'max_salary']

	def __init__(self, *args, **kwargs):
		super(JobFilter, self).__init__(*args, **kwargs)
		self.filters['level'].extra.update(
			{'empty_label': 'All'})
		self.filters['city'].extra.update(
			{'empty_label': 'All'})
