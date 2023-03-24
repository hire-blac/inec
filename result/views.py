from django.shortcuts import render

# Create your views here.
def show(response):
    response.write("show result")