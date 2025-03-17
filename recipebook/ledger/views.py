from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):
    '''
    Creates a base view for displaying the list of recipes.
    '''
    context_object_name = "recipes"
    queryset = Recipe.objects.all()
    template_name = "recipes.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    '''
    Creates a base view for displaying the contents of each recipe.
    '''
    context_object_name = "recipe"
    model = Recipe
    template_name = "recipe.html"