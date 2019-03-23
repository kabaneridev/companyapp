from django import forms
from django.forms import ModelForm
from .models import Job, Company, LEVELS, Stack, Emp_type, CITIES
from django.core.validators import MinValueValidator
from .validators import validate_doc_or_pdf

class ContactForm(forms.Form):
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

# form  applying for job

class JobApply(forms.Form):
	first_name = forms.CharField(required=True, max_length=30)
	last_name = forms.CharField(required=True, max_length=30)
	from_email = forms.EmailField(required=True)
	CV = forms.FileField(required=True, validators=[validate_doc_or_pdf])
	cover_letter = forms.FileField(required=False, validators=[validate_doc_or_pdf])
	job_name = Job.name
	job_company = Job.company
	send_to = Job.contact_email
