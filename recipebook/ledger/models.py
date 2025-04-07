from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    Extends User model, accepts name and bio.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    '''
    Accepts ingredient name.
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])

class Recipe(models.Model):
    '''
    Accepts recipe name and author name, automatically adds date and time created and modified.
    '''
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])

class RecipeIngredient(models.Model):
    '''
    Connects recipe and ingredient models, also accepts quantity.
    '''
    Quantity = models.CharField(max_length=100)
    Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
        )
    Recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name="ingredients"
        )
    
class RecipeImage(models.Model):
    '''
    Accepts image, description, and recipe.
    '''
    image = models.ImageField(null=False, upload_to="images/")
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe"
    )

    def __str__(self):
        return self.description