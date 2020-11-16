
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

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)

        message = f"{search_term}"

        return render(request, 'search_results.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})