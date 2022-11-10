from unicodedata import name
from django.shortcuts import render, redirect
from home.models import Car
# from home.models import Car, CarUser
from home.forms import SearchCarForm, CarForm
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')
    
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
        
        # users = CarUser.objects.filter(user=request.user.id) 
        
        form =CarForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            car_fabricant = data['car_fabricant']
            car_model = data['car_model']
            car_type = data['car_type']
            car_color = data['car_color']
            car_year = data['car_year']
            fabrication_date =  data.get('fabrication_date')
            car_description = data['car_description']
            posted_by = data['posted_by']
            car_image = data['car_image']
            
            if fabrication_date == None:
                fabrication_date = datetime.now()
            
            car = Car(car_fabricant = car_fabricant, 
                    car_model = car_model, 
                    car_type = car_type,
                    car_color = car_color,
                    car_year = car_year,
                    fabrication_date = fabrication_date,
                    car_description = car_description,
                    posted_by = posted_by,
                    car_image = car_image)
            
            car.save()
            return redirect('view_cars')
    
    form = CarForm()
    return render(request, 'home/create_car.html', {'form' : form})

class EditCar(LoginRequiredMixin,UpdateView):
    model = Car
    success_url = '/cars/'
    template_name = 'home/edit_car.html'
    fields = ['car_fabricant',
            'car_model',
            'car_type',
            'car_color',
            'car_year',
            'fabrication_date',
            'car_description',
            'posted_by',
            'car_image']

class DeleteCar(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'home/delete_car.html'
    
class CarDetails(DetailView):
    model = Car
    template_name = 'home/car_details.html'