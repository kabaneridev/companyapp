from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Company
from .filters import CompanyFilter
from rest_framework import viewsets
from .serializers import CompanySerializer
# Create your views here.

def companies_list(request):
    my_companies = Company.objects.all()

    ## filter by company type
    type = request.GET.get('type')
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

##def brands(request, slug):
  ##  brands = Company.objects.all()
    ##return render(request, 'company/comp_view.html', {'brands': brands})

def brands(request, pk):
    brand = get_object_or_404(Company, pk=pk)
    return render(request, 'company/comp_view.html', {'brand': brand})

#rest api


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer