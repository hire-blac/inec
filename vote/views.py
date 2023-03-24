from django.shortcuts import render

# Create your views here.
def vote(response):
    response.write("Voted")