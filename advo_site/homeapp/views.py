from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home_index(request: HttpRequest):
    print(request.path)
    return render(request, 'homeapp/index.html')
