# recipes/urls.py 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),  # Home page
    path('all_recipes/', views.RecipeListView.as_view(), name="recipes-all_recipes"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('about/', views.about, name="recipes-about"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
]