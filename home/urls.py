from django.urls import path
from home import views


urlpatterns = [
    path('', views.index_bootstrap, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('cars/', views.view_cars, name='view_cars'),
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/edit/<int:pk>', views.EditCar.as_view(), name='edit_car'),
    path('cars/delete/<int:pk>', views.DeleteCar.as_view(), name='delete_car'),
    path('cars/details/<int:pk>', views.CarDetails.as_view(), name='car_details'),
]    