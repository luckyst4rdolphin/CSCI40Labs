from django.urls import path
from . import views

urlpatterns = [
    
    path('recipes/list/', views.recipe_list, name="recipes-list"),
    path('recipe/<int:id>/', views.recipe_detail, name="recipe-detail")
]

app_name = "ledger"