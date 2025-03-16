from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    '''
    accepts ingredient name
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])

class Recipe(models.Model):
    '''
    accepts recipe name and author name, automatically adds date and time created and modified
    '''
    name = models.CharField(max_length=100),
    author = models.CharField(max_length=100),
    created_on = models.DateTimeField(auto_now_add=True),
    updated_on = models.DateTimeField(auto_now=True),

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])

class RecipeIngredient(models.Model):
    '''
    connects recipe and ingredient models
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

class Profile(models.Model):
    '''
    extends User model, accepts name and bio
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)
    