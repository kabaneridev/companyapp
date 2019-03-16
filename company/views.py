from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, FormView
from .models import Company
from .forms import ContactCompanyForm
from .filters import CompanyFilter
from rest_framework import viewsets
from .serializers import CompanySerializer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def comp_list(request):
    f = CompanyFilter(request.GET, queryset=Company.objects.all())
    return render(request, 'company/comp_list.html', {'filter': f})

def companies(request):
    company = get_object_or_404(Company)
    return render(request, 'company/comp_list.html', {'company': company})

def home(request):
    return render(request, 'company/home.html')

def brands(request, slug):
    brand = get_object_or_404(Company, slug=slug)
    return render(request, 'company/comp_view.html', {'brand': brand})

#rest api
class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# modal contact company add form

def emailView(request):
    if request.method == 'GET':
        form = ContactCompanyForm()
    else:
        form = ContactCompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            from_email = form.cleaned_data['from_email']
            phone_number = form.cleaned_data['phone_number']
            try:
                send_mail('Contact Form', company, from_email, ['krplominski@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "company/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')