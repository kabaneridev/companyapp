from django.urls import path
from django.conf.urls import url
from . import views
from django_filters.views import object_filter
from company.models import Company
from .views import emailView, successView

urlpatterns = [
	path('', views.home, name='home'),
	path('brands/', views.comp_list, name='comp_list'),	
	path('brands/<slug:slug>/', views.brands, name='comp_view'),
    url(r'^list/$', object_filter, {'model': Company}),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
    path('jobs/', views.job_list, name="job_list"),
    #path('jobs/<slug:slug>/', views.jobs, name='job_view'),
]
