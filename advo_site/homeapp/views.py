from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import time
import datetime


def home_index(request: HttpRequest):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'homeapp/index.html', context=context)


def team_view(request: HttpRequest):
    context = {
        'title': 'Команда'
    }
    return render(request, 'homeapp/team.html', context=context)


def cases_view(request: HttpRequest):
    context = {
        'title': 'Кейсы'
    }
    return render(request, 'homeapp/cases.html', context=context)


def career_view(request: HttpRequest):
    context = {
        'title': 'Карьера'
    }
    return render(request, 'homeapp/career.html', context=context)


def about_view(request: HttpRequest):
    context = {
        'title': 'О нас'
    }
    return render(request, 'homeapp/about.html', context=context)
