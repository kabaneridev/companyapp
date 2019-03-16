from django import forms

class ContactCompanyForm(forms.Form):
    name = forms.CharField(max_length=150)
    company = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=13, required=True)