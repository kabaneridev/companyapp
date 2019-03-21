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

class PostJob(forms.Form):
	class Meta:
		model = Job
		name = forms.CharField(max_length=40)
		level = forms.CharField(
			max_length=10,
			widget=forms.Select(choices=LEVELS),
		)
		stack = forms.ModelMultipleChoiceField(Stack.objects.all(), required=True)
		emp_type = forms.ModelMultipleChoiceField(Emp_type.objects.all(), required=True)
		min_salary = forms.IntegerField(validators=[MinValueValidator(1)], required=True)
		max_salary = forms.IntegerField(required=True)
		description = forms.CharField(
			required=True,
			widget=forms.Textarea,
		)
		city = forms.CharField(
			max_length=20,
			widget=forms.Select(choices=CITIES),
		)