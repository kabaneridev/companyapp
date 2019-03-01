from django.urls import path
from . import views

urlpatterns = [
    path('', views.companies_list, name='companies_list'),

]
