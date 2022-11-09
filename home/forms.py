from unicodedata import name
from django import forms
from ckeditor.fields import RichTextFormField
    
class CarForm(forms.Form):
    car_fabricant = forms.CharField(max_length=20)
    car_model = forms.CharField(max_length=20)
    car_type = forms.CharField(max_length=20)
    car_color = forms.CharField(max_length=20)
    car_year = forms.IntegerField()
    fabrication_date = forms.DateField(required=False)    
    car_description = RichTextFormField(required=False)
    
class SearchCarForm(forms.Form):
    car_fabricant = forms.CharField(max_length=30, required=False)