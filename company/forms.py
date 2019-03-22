from django import forms
from django.forms import ModelForm
from .models import Job, Company, LEVELS, Stack, Emp_type, CITIES
from django.core.validators import MinValueValidator

class ContactCompanyForm(forms.Form):
    name = forms.CharField(max_length=150)
    company = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=13, required=True)

# form for posting job

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = [
			'name',
			'level',
			'stack',
			'emp_type',
			'min_salary',
			'max_salary',
			'description',
			'city',
			'company'
		]

