from django.shortcuts import render

from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Business
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


from django.views import generic

from .models import Login


def login(request):
    return render(request, 'open_now/login.html')


class LoginView(generic.ListView):
    template_name = 'open_now/login.html'

    def get_queryset(self):
        """
        """
        return

class HomeView(generic.ListView):
    template_name = 'open_now/home.html'

    def get_queryset(self):
        """
        """
        return

class BusinessView(generic.ListView):
    template_name = 'open_now/business_list.html'
    context_object_name = 'business_list'

    def get_queryset(self):
        """
        """
        return Business.objects.all()
        return

class BusinessFormView(generic.ListView):
    template_name = 'open_now/business_form.html'

    def get_queryset(self):
        """
        """
        return

def get_business(request):

    business_name = request.POST['business_name']
    description = request.POST['description']
    t = Business(business_name=business_name,description=description, phone_number = 1232310912, website = 'asd.com',
                 business_category = "REST")
    t.save()
    return HttpResponseRedirect(reverse('open_now:business_list'))
