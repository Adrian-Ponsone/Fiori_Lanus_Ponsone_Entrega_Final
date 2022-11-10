###BLOG ABOUT CARS###

to enjoy this blog you will need:
asgiref==3.5.2
Django==4.1.3
Pillow==9.3.0
sqlparse==0.4.3
tzdata==2022.6

in this code you will find:
---------------------------------------------------------------------------------------------------------
register.html: where you register a user with email and password

login.html: necessary to access a more features of the page

(Completing these sections will unlock new accesses in the nav)

about.html: there is information about the creation of the blog

profile.html: there is information about your account and you can edit this information whenever you want in edit_profile.html

logout.html: on this page you can close your session

create_car.html(login required): here you can create a car based on different aspects such as its manufacturer or its color

view_cars.html: here you can see the cars created

edit_car.html: to edit your cars

delete_car.html: to delete a car

---------------------------------------------------------------------------------------------------------------

####¿how to make the code work correctly?####

---------------------------------------------------------------------------------------------------------------
1.Clone the repository

2.Once opened, create the virtual enviroment and activate it with "venv/Scripts/activate"

3.Install Django with "pip install django" at the cmd and verify that is working correctly

4.Install pillow with "python -m pip install Pillow"

5.Install ckeditor with "pip install django-ckeditor"

6.Make the migrations in the cmd with "py manage.py migrate" for create the database

7.Start the development server with "py manage.py runserver"

8.Open the http link with (ctrl + click)

9.enjoy the blog!!

Superuser
user: admin
pass: 123456
--------------------------------------------------------------------------------------------------------------

by Agustín Fiori, Adrian Ponsone and Agustin Lanus
