from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Company
from .filters import CompanyFilter
from rest_framework import viewsets
from .serializers import CompanySerializer

def comp_list(request):
    f = CompanyFilter(request.GET, queryset=Company.objects.all())
    return render(request, 'company/comp_list.html', {'filter': f})

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