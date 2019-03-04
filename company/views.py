from django.shortcuts import render
from django.utils import timezone
from .models import Company
from .filters import CompanyFilter
# Create your views here.

def companies_list(request):
    my_companies = Company.objects.all()

    type = request.GET.get('type')
    ## filter by company type
    if type:
        my_companies = Company.objects.filter(type=type)
    ## filter by company city
    city = Company.objects.all()
    if city:
        my_companies = Company.objects.filter(city=city)
    ## filter by company technologies
    stack = request.GET.get('stack')
    if stack:
        my_companies = Company.objects.filter(city=city)

    my_companies = my_companies.order_by('published_date')
    return render(request, 'company/companies_list.html', {'my_companies': my_companies})

def comp_list(request):
    f = CompanyFilter(request.GET, queryset=Company.objects.all())
    return render(request, 'company/comp_list.html', {'filter': f})