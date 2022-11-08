from unicodedata import name
from django.shortcuts import render, redirect
from home.models import Car
from home.forms import SearchCarForm, CarForm
from django.shortcuts import render, redirect
from datetime import datetime
# from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')

# class ListCars(ListView):
#     model = Car
#     template_name = 'home/view_cars.html'
    
def view_cars(request):
   
    car_fabricant = request.GET.get('car_fabricant', None)
    if car_fabricant:
        cars = Car.objects.filter(car_fabricant__icontains=car_fabricant)
    else:
        cars = Car.objects.all()
        
    form = SearchCarForm()
    return render(request, 'home/view_cars.html', {'cars' : cars, 'form' : form})

@login_required
def create_car(request):
    if request.method == 'POST':
        
        form =CarForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            car_fabricant = data['car_fabricant']
            car_model = data['car_model']
            car_type = data['car_type']
            car_color = data['car_color']
            car_year = data['car_year']
            fabrication_date =  data.get('fabrication_date')
            if fabrication_date == None:
                fabrication_date = datetime.now()
            
            car = Car(car_fabricant = car_fabricant, 
                      car_model = car_model, 
                      car_type = car_type,
                      car_color = car_color,
                      car_year = car_year,
                      fabrication_date = fabrication_date)
            car.save()
            return redirect('view_cars')
    
    form = CarForm()
    return render(request, 'home/create_car.html', {'form' : form})

# class CreateCar(LoginRequiredMixin, CreateView):
#     model = Car
#     success_url = '/cars/'
#     template_name = 'home/create_car.html'
#     fields = ['car_fabricant',
#               'car_model',
#               'car_type',
#               'car_color',
#               'car_year',
#               'fabrication_date']
    
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
    