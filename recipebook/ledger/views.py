from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm, IngredientForm
from django.urls import reverse_lazy

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
    extra_context = {"images":RecipeImage.objects.all}

class RecipeCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates base view for a new recipe form.
    '''
    model = Recipe
    template_name = "recipe_form.html"
    form_class = RecipeForm
    success_url = "/recipe/add/recipeingredient/"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)
        context['recipe_form'] = context['form']
        return context

class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates base view for recipe ingredient or recipe detail form.
    '''
    model = RecipeIngredient
    template_name = "recipeingredient_form.html"
    form_class = RecipeIngredientForm
    success_url = reverse_lazy('ledger:recipes-list')

    def get_context_data(self, **kwargs):
        context = super(RecipeIngredientCreateView, self).get_context_data(**kwargs)
        context['recipeingredient_form'] = context['form']
        return context
    
class IngredientCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates a base view for the new ingredient form.
    '''
    model = Ingredient
    template_name = "ingredient_form.html"
    form_class = IngredientForm
    success_url = "/recipe/add/recipeingredient/"

    def get_context_data(self, **kwargs):
        context = super(IngredientCreateView, self).get_context_data(**kwargs)
        context['ingredient_form'] = context['form']
        return context
    
class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates a base view for the new recipe image form.
    '''
    model = RecipeImage
    template_name = "recipeimage_form.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={ 'pk': self.object.recipe.pk })

    def get_context_data(self, **kwargs):
        context = super(RecipeImageCreateView, self).get_context_data(**kwargs)
        context['recipeimage_form'] = context['form']
        return context