# recipes/urls.py 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    # Add more URL patterns here as needed
]