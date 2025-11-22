from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe

# Create your views here.

# esse for serve para gerar 10 ou mais conteudo dinamicamente
# mas tem que criar o stript de automação

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request,category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def recipe(request,id):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
        
    })


   
