from unicodedata import name
from django.shortcuts import render, redirect

def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')
