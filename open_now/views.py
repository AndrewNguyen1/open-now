from django.shortcuts import render

from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Business, Forum, Discussion
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import * 
from django.shortcuts import redirect


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
    phone_number = request.POST['phone_number']
    website = request.POST['website']
    business_category = request.POST['business_category']
    t = Business(business_name=business_name,description=description, phone_number = phone_number, website = website,
                 business_category = business_category)
    t.save()
    return HttpResponseRedirect(reverse('open_now:business_list'))

def search_business(request):
    srh = request.GET['query']
    businesses = Business.objects.filter(business_name__icontains=srh) | Business.objects.filter(description__icontains=srh) | Business.objects.filter(business_category__icontains=srh)
    params={'businesses': businesses, 'search':srh}
    return render(request, 'open_now/search_business.html', params)

def new_forum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/open_now/forums')
    context ={'form':form}
    return render(request,'open_now/new_forum.html',context)
 
def new_discussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/open_now/forums')
    context ={'form':form}
    return render(request,'open_now/new_discussion.html',context)

def forums(request):
    all_forums=Forum.objects.all()
    count=all_forums.count()
    discussions=[]
    for i in all_forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':all_forums,
            'count':count,
            'discussions':discussions}
    return render(request,'open_now/forums.html',context)