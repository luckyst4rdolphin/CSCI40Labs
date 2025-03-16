from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    context_object_name = "recipes"
    queryset = Recipe.objects.all()
    template_name = "recipes.html"

class RecipeDetailView(DetailView):
    context_object_name = "recipe"
    model = Recipe
    template_name = "recipe.html"