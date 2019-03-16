from django import forms
from .models import AddCompany
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class AddCompanyForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = AddCompany
        fields = ['name', 'company_name', 'email', 'phone_number']