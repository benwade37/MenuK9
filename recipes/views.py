# recipes/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe

from . import models

class RecipeListView(LoginRequiredMixin, ListView):
  model = models.Recipe
  template_name = 'recipes/all_recipes.html'
  context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = models.Recipe

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = models.Recipe
  fields = ['title', 'description']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  fields = ['title', 'description']

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})

def all_recipes(request):
    recipes = Recipe.objects.all()  # Fetch all recipes from the database
    return render(request, 'recipes/all_recipes.html', {'recipes': recipes})

def home(request):
    return render(request, 'recipes/home.html', {'title': 'Home'})