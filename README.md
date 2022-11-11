###BLOG ABOUT CARS###

to enjoy this blog you will need:
asgiref==3.5.2
Django==4.1.3
Pillow==9.3.0
sqlparse==0.4.3
tzdata==2022.6
django-ckeditor==6.5.1
django-js-asset==2.0.0

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
1.Clone the repository using "git clone link_github".   

2.Once opened, create the virtual enviroment and activate it with ". virtual_enviroment_name/Scripts/activate".

3.Once activated, install Django with "pip install django" at the terminal and verify that is working correctly.

4.Install pillow with "python -m pip install Pillow".

5.Install ckeditor with "pip install django-ckeditor".

6.Make the migrations in the terminal to create the database:
    For make the migrations use:    py manage.py makemigrations
                                    py manage.py migrate

7.Run the project with "py manage.py runserver".

8.Open the http link with (ctrl + click).

9.First you will have to register with an user name and a password, if you don't signup you wouldn't able to post, edit or eliminate
  the cars previusly created but if you aren't log you still can see the list car history created to the moment.

10.To use the section of admin you will have to create a superuser with py manage.py created superuser and login as superuser.

11.Finally, enjoy the blog!!.
--------------------------------------------------------------------------------------------------------------

by Agustín Fiori, Adrian Ponsone and Agustin Lanus

explanatory video of the project in: https://drive.google.com/drive/folders/1LwKnaW1_noPlAs5uEZiZHUUGPJte9K87?usp=share_link
