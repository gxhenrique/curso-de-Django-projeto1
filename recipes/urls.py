from django.urls import path

# from recipes.views import home

from recipes.views import home
from recipes.views import recipe
from recipes.views import category

#criar "name" para as url para que elas fiquem dinamicas

app_name = 'recipes'

urlpatterns = [
    path('', home, name= 'recipes-home'),
    path('recipes/category/<int:category_id>/', category, name= 'category'),
    path('recipes/<int:id>/', recipe, name= 'recipes-recipe')
   
]

#  path('recipes/category/<int:category_id>/',
#          views.category, name="category"),