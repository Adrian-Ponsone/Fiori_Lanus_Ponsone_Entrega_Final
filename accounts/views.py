from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import MyCreationForm, FormProfileEdit
from accounts.models import UserExtension


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)    
            userextension, is_new = UserExtension.objects.get_or_create(user=request.user)
            return redirect('index')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form' : form})

def register(request):
    if request.method == 'POST':
        form = MyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyCreationForm()
        
    return render(request, 'accounts/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})

@login_required
def edit_profile(request):
    
    if request.method == 'POST':
        form = FormProfileEdit(request.POST, request.FILES)
        
        if form.is_valid():
            new_data = form.cleaned_data
            request.user.first_name = new_data['first_name']
            request.user.last_name = new_data['last_name']
            request.user.email = new_data['email']
            request.user.userextension.avatar = new_data['avatar']
            
            request.user.userextension.save()
            request.user.save()
            return redirect('profile')
        
    else:
        form = FormProfileEdit(initial={'first_name' : request.user.first_name,
                                        'last_name' : request.user.last_name,
                                        'email' : request.user.email,
                                        'avatar' : request.user.userextension.avatar})
    
    return render(request, 'accounts/edit_profile.html', {'form' : form})


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = '/accounts/profile/'