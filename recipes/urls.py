from recipes.views import home
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe)

]
