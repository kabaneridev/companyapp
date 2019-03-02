from django.urls import path
from django.conf.urls import url
from . import views
from django_filters.views import object_filter
from company.models import company

urlpatterns = [
##	temporary disabled
##	path('', views.companies_list, name='companies_list'),
##    path('brands', views.comp_list, name='comp_list'),
    url(r'^search$', views.comp_list),
    url(r'^list/$', object_filter, {'model': company}),

]
