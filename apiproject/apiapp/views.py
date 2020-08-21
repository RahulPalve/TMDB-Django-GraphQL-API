from django.shortcuts import render,HttpResponse
from .populate_db import populate


# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def populateDB(request):
    populate()
    return HttpResponse("Database Populated..")


    