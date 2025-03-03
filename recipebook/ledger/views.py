from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(recipe_id=id)
    recipe_ingredients = Ingredient.objects.filter(recipe__recipe__name=f"Recipe{recipe_id}")
    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }
    return render(request, 'recipe.html', context)