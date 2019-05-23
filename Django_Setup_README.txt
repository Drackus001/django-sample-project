pip3 install virtualenv : installing virtualenv

pip3 freeze : for showing install packages

virtualenv -p /usr/bin/python3.7 venv : creating venv folder in directory

source venv/bin/activate : for activating virtualenv

pip3 install Django :installing Django on virtualenv

django-admin.py startproject MyWeb :Creating Django-Project with MyWeb directory

python manage.py runserver : Create server for Django

python manage.py createsuperuser : used for creating users/admin for project_database

python manage.py migrate :Used for migrate in-built database files to properly

python manage.py startapp pages : Used to create/start the pages folder

python manage.py makemigrations : used for after creating the database in models.py

python manage.py sqlmigrate pages 0001 : used for see SQL Query for in terminal

python manage.py shell : used for open python shell in terminal

	 from pages.models import Post
	from django.contrib.auth.models import User

pip3 install django-crispy-forms : Used for get design for user registration
