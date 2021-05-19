from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.shortcuts import HttpResponse   

 
#from formValidationApp.models import * 
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):

    return render(request,'about-us.html')
def team(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')