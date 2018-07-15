from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def index(req):
    x = "Hello World"
    return render(req, 'application/base.html', {'x':x})
