from django.urls import path
from django.conf.urls import url
from . import views
from django_filters.views import object_filter
from company.models import Company
from .views import AddCompany

urlpatterns = [
	path('', views.home, name='home'),
	path('brands/', views.comp_list, name='comp_list'),	
	path('brands/<slug:slug>/', views.brands, name='comp_view'),
	path('add_company/', AddCompany.as_view(), name='add_company'),
    url(r'^list/$', object_filter, {'model': Company}),
]
