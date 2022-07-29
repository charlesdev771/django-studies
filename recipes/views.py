from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/recipes/pages/home.html',context={
        'name': 'Charles Dantas',
    })

def recipe(request, id):
    return render(request, 'recipes/recipes/pages/recipe-view.html', context={
        'name': 'Teste',
    })
