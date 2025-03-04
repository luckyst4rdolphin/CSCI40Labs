from django.shortcuts import render
from .models import Recipe, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe_ingredient = RecipeIngredient.objects.filter(Recipe = recipe)
    context = {
        'recipe': recipe,
        'recipe_ingredient': recipe_ingredient,
    }
    return render(request, 'recipe.html', context)