from django import forms
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient

class RecipeForm(forms.ModelForm):
    '''
    Creates model form for adding new recipe.
    '''
    class Meta:
        model = Recipe
        fields = ["name"]

class RecipeIngredientForm(forms.ModelForm):
    '''
    Creates model form for adding new recipe details.
    '''
    class Meta:
        model = RecipeIngredient
        fields = ["Recipe", "Ingredient", "Quantity"]

class IngredientForm(forms.ModelForm):
    '''
    Creates model form for adding new ingredients.
    '''
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeImageForm(forms.ModelForm):
    '''
    Creates model form for adding new recipe image.
    '''
    class Meta:
        model = RecipeImage
        fields = "__all__"