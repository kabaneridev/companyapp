from django.urls import path
from . import views

urlpatterns = [
	path('', views.companies_list, name='companies_list'),
    path('brands', views.companies_list, name='companies_list'),

path('all/star', views.companies_list, name='companies_list'),
]
