from unicodedata import name
from django import forms
from ckeditor.fields import RichTextFormField
    
class CarForm(forms.Form):
    car_fabricant = forms.CharField(max_length=20)
    car_model = forms.CharField(max_length=20)
    car_type = forms.CharField(max_length=20, label='Sedan or QP')
    car_color = forms.CharField(max_length=20)
    car_year = forms.IntegerField()
    fabrication_date = forms.DateField(required=False, label='Fabrication date (mm/dd/yyyy)')    
    car_description = RichTextFormField(required=False)
    posted_by = forms.CharField(required = False, max_length=20, label='Posted By')
    car_image = forms.ImageField(required = False, label='Load an image')
        
class SearchCarForm(forms.Form):
    car_fabricant = forms.CharField(max_length=30, required=False)