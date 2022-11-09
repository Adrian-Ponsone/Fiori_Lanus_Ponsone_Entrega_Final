from django.db import models
from ckeditor.fields import RichTextField

class Car(models.Model):
    car_fabricant = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_type = models.CharField(max_length=20)
    car_color = models.CharField(max_length=20)
    car_year = models.IntegerField()
    fabrication_date = models.DateField()
    car_description = RichTextField(null=True)
    
    def __str__(self):
        return f'Fabricant: {self.car_fabricant} - Model: {self.car_model} - Type: {self.car_type} Color: {self.car_color}'