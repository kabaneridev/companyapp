from django.urls import path
from django.conf.urls import url
from . import views
from django_filters.views import object_filter
from company.models import Company

urlpatterns = [
##	temporary disabled
	path('', views.comp_list, name='comp_list'),
	##('brands', views.comp_list, name='comp_list'),
    url(r'^brands$', views.comp_list),
    url(r'^list/$', object_filter, {'model': Company}),

]
