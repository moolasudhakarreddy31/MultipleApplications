from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish1(request):
    return HttpResponse('<h1>Hi This is First App Aplication</h1>')