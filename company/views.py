from django.shortcuts import render
from django.utils import timezone
from .models import company
# Create your views here.

def companies_list(request):
    my_companies = company.objects.filter(
        published_date__lte=timezone.now())


    company_types = request.GET.get('company_types')
    if company_types:
        my_companies = company.objects.filter(company_types=company_types)

    city = request.GET.get('city')
    if city:
        my_companies = company.objects.filter(city=city)




    my_companies = my_companies.order_by('published_date')
    return render(request, 'company/companies_list.html', {'my_companies': my_companies})



