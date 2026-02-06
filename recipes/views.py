from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormView
from django.http import HttpResponseForbidden

from .models import Recipe, Rating
from .forms import RecipeForm, RatingForm

# ---------- Static pages ----------

def home(request):
    return render(request, "recipes/home.html")

def about(request):
    return render(request, "recipes/about.html")

# ---------- Recipes ----------

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/all_recipes.html"
    context_object_name = "recipes"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RatingForm()

        # Check if the user has already rated this recipe
        context["has_rated"] = self.object.ratings.filter(user=self.request.user).exists()

        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = "draft"
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ["title", "description", "steps", "image"]

    def test_func(self):
        return self.get_object().author == self.request.user


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes-all_recipes")

    def test_func(self):
        return self.get_object().author == self.request.user


class SubmitRatingView(LoginRequiredMixin, FormView):
    form_class = RatingForm

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs["pk"])

        if Rating.objects.filter(user=self.request.user, recipe=recipe).exists():
            return HttpResponseForbidden("You have already submitted a rating for this recipe.")

        Rating.objects.create(
            user=self.request.user,
            recipe=recipe,
            rating=form.cleaned_data["rating"]
        )

        return redirect("recipes-detail", pk=recipe.pk)

