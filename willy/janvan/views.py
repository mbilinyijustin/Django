from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def mbilinyi(request):
    #return HttpResponse("Hello world!")
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
