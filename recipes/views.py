from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def contato(request):
    return HttpResponse('contact')

def about(request):
    return HttpResponse('About')
