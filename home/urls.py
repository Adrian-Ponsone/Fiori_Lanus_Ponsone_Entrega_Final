from django.urls import path
from home import views


urlpatterns = [
    path('', views.index_bootstrap, name='index'),
    path('about-us/', views.about_us, name='about-us'),
]    