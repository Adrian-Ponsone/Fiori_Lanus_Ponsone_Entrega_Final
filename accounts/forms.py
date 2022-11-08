from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MyCreationForm(UserCreationForm):
    
    email = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 
                  'email', 
                  'password1',
                  'password2']
        help_texts = {key: ' ' for key in fields }
        
class FormProfileEdit(forms.Form):
    first_name = forms.CharField(label = 'Name')
    last_name = forms.CharField(label = 'Last Name')
    email = forms.CharField()
    avatar = forms.ImageField(required=False)