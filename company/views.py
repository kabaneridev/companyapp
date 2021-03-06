from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView
from .models import Company, Stack, Position, Job
from .forms import ContactForm, JobForm, JobApply
from .filters import CompanyFilter, JobFilter
from rest_framework import viewsets
from .serializers import CompanySerializer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# view for companies list

def comp_list(request):
    f = CompanyFilter(request.GET, queryset=Company.objects.all())
    return render(request, 'company/comp_list.html', {'filter': f})

# view for home page

def home(request):
    return render(request, 'company/home.html')

# view for posting job
@login_required
def post_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    
    return render(request, 'company/post_job.html', context)

# view for companies on company page

def brands(request, slug):
    brand = get_object_or_404(Company, slug=slug)
    return render(request, 'company/comp_view.html', {'brand': brand})

# view for job list

def job_list(request):
    f = JobFilter(request.GET, queryset=Job.objects.all())
    return render(request, 'company/job_list.html', {'filter': f})

# view for job offer

def jobs(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'company/job_view.html', {'job': job})

#rest api

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# modal contact company add form

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            from_email = form.cleaned_data['from_email']
            phone_number = form.cleaned_data['phone_number']
            try:
                send_mail('Contact Form', company, from_email, ['krplominski@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "company/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# view for job applying form

def jobApply(request):
    if request.method == 'GET':
        form = JobApply()
    else:
        form = JobApply(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            from_email = form.cleaned_data['from_email']
            CV = form.cleaned_data['CV']
            cover_letter = form.cleaned_data['cover_letter']
            job_name = job_name
            job_company = job_company
            send_to = send_to
            try:
                send_mail('Job apply form', first_name, last_name, from_email, CV, job_name, job_company, ['send_to'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "company/job_apply.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

