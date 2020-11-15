from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    return HttpResponse('Hello')