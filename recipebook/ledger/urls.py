from django.urls import path
from .views import recipelist, recipe_one, recipe_two

urlpatterns = [
    path('recipes/list/', recipelist, name="recipelist"),
    path('recipe/1/', recipe_one, name="recipe1"),
    path('recipe/2', recipe_two, name="recipe2")
]

app_name = "ledger"