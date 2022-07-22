from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/recipes/pages/home.html',context={
        'name': 'Charles Dantas',
    })
