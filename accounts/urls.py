from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/edit/', views.edit_profile, name = 'edit_profile'),
    path('profile/change-password/', views.ChangePassword.as_view(), name = 'change_password')
]
