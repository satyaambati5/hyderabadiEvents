from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.shortcuts import HttpResponse    
from django.http import HttpResponseRedirect
from .models import scroler,gallery_photo
# Create your views here.
def home(request):
    data_scroler=scroler.objects.all()
    return render(request,"index.html",{'data_scroler':data_scroler})
    # return render(request,"index.html")


def about(request):

    return render(request,'about-us.html')
def gallery(request):
    data_gallery=gallery_photo.objects.all()
    return render(request,"gallery.html",{'data_gallery':data_gallery})
    # return render(request,"gallery.html")
def contact(request):
    return render(request,'contact.html')
# def scroler_data(request):
#     data_scroler=scroler.objects.all()
#     return render(request,"index.html",{'data_scroler':data_scroler})