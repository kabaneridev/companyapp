from django.shortcuts import render
from django.utils import timezone
from .models import company
from .filters import CompanyFilter
# Create your views here.

def companies_list(request):
    my_companies = company.objects.filter(
        published_date__lte=timezone.now())


    type = request.GET.get('type')
    ## filter by company type
    if type:
        my_companies = company.objects.filter(type=type)
    ## filter by company city
    city = request.GET.get('city')
    if city:
        my_companies = company.objects.filter(city=city)
    ## filter by company technologies
    stack = request.GET.get('stack')
    if stack:
        my_companies = company.objects.filter(stack=stack)


    my_companies = my_companies.order_by('published_date')
    return render(request, 'company/companies_list.html', {'my_companies': my_companies})

def comp_list(request):
    f = CompanyFilter(request.GET, queryset=company.objects.all())
    return render(request, 'company/comp_list.html', {'filter': f})