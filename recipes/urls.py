from django.urls import path
from recipes.views import contato, about, home


urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('contato/', contato)
]