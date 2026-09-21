from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Home, world. You're at the usuarios index.")

def hello (request, name):
    return HttpResponse(f"Hello, {name}. You're at the usuarios index.")

def chau (request):
    return HttpResponse("Chau, world. You're at the usuarios index.")