from django.db import models
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import User

class Car(models.Model):
    car_fabricant = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_type = models.CharField(max_length=20)
    car_color = models.CharField(max_length=20)
    car_year = models.IntegerField()
    fabrication_date = models.DateField()
    car_description = RichTextField(null=True)
    posted_by = models.CharField(null = True, max_length=20)
    car_image = models.ImageField(upload_to = 'cars', null=True, blank=True)
    # car_user = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f'Fabricant: {self.car_fabricant} - Model: {self.car_model} - Type: {self.car_type}'
    
# class CarUser(models.Model):
        # car_user = models.ForeignKey(User, on_delete=models.CASCADE)