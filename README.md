This is a repository built as part of HPE's training program. This project is an inventory stock management system built using Django. Features implemented use routing, authentication and database management to learn the fundamentals of Django.

1) Clone the repository and set up a virtual environment

2) For this project, we require the Django and rest-framework packages which can be installed using 
```python
pip install django rest-framework
```

3) Run the following command in terminal to register yourself as a superuser to access the products and perform operations
```python
python manage.py createsuperuser
```
4) Then run the server using python manage.py runserver

5) Open http://127.0.0.1:8000/ on your browser to run the project

6) Use the endpoint /products to access products. We have used the inbuilt browser template to create a form that will simulate requests like /POST, /PUT, etc to the backend and show results.
