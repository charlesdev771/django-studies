from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/index.html',context={
        'name': 'Charles Dantas',
    })

def contato(request):
    return HttpResponse('contact')

def about(request):
    return HttpResponse('About')
