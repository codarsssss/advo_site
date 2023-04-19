from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import time
import datetime


def home_index(request: HttpRequest):
    return render(request, 'homeapp/index.html')


def about_us_index(request: HttpRequest):
    return render(request, 'homeapp/about-us.html')
