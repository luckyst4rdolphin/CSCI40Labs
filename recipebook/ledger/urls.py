from django.urls import path
from .views import recipeList, recipeOne, recipeTwo

urlpatterns = [
    path('recipes/list/', recipeList, name="recipelist"),
    path('recipe/1/', recipeOne, name="recipe1"),
    path('recipe/2', recipeTwo, name="recipe2")
]

app_name = "ledger"