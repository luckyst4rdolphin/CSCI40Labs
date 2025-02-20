from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('recipelist.html')
    return HttpResponse(template.render())

#def tasks(request):
    #ctx = 
