from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('my-profile/', views.my_profile, name='my-profile'),  # Correct view reference
]