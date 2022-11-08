from django.urls import path
from home import views


urlpatterns = [
    path('', views.index_bootstrap, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('cars/', views.ListCars.as_view(), name='view_cars'),
    path('cars/create/', views.CreateCar.as_view(), name='create_car'),
    path('cars/edit/<int:pk>', views.EditCar.as_view(), name='edit_car'),
    path('cars/delete/<int:pk>', views.DeleteCar.as_view(), name='delete_car'),
]    