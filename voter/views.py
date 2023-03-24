from django.shortcuts import render

# Create your views here.

def register(response):
    response.write('Register new voter')

def show(response):
    response.write('Show voter details')