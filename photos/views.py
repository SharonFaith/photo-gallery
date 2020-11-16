
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

from django.core.exceptions import ObjectDoesNotExist
from .models import Image, Category, Location

# Create your views here.
def welcome(request):

   return redirect(index)

def index(request):

    photos = Image.get_all_images()
    

    return render(request, 'index.html', {'photos': photos})