from unicodedata import name
from django.shortcuts import render, redirect
from home.models import Car
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')

class ListCars(ListView):
    model = Car
    template_name = 'home/view_cars.html'

class CreateCar(LoginRequiredMixin, CreateView):
    model = Car
    success_url = '/cars/'
    template_name = 'home/create_car.html'
    fields = ['car_fabricant',
              'car_model',
              'car_type',
              'car_color',
              'car_year',
              'fabrication_date']
    
class EditCar(LoginRequiredMixin,UpdateView):
    model = Car
    success_url = '/cars/'
    template_name = 'home/edit_car.html'
    fields = ['car_fabricant',
              'car_model',
              'car_type',
              'car_color',
              'car_year',
              'fabrication_date']

class DeleteCar(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'home/delete_car.html'
    