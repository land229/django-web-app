from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>') 

def about(request):
    return HttpResponse('<h1>We are the world!</h1>') 
