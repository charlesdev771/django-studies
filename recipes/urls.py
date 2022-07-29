from recipes.views import home
from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe")
]
