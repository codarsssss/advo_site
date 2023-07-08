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


def zashchita_view(request: HttpRequest):
    context = {
        'title': 'Защита при уголовном преследовании'
    }
    return render(request, 'homeapp/zashchita.html', context=context)


def business_view(request: HttpRequest):
    context = {
        'title': 'Уголовно-правовая защита бизнеса'
    }
    return render(request, 'homeapp/business.html', context=context)


def antikorruptsionnoe_view(request: HttpRequest):
    context = {
        'title': 'Антикоррупционное просвещение'
    }
    return render(request, 'homeapp/antikorruptsionnoe.html', context=context)


def semeynoe_view(request: HttpRequest):
    context = {
        'title': 'Семейное право'
    }
    return render(request, 'homeapp/semeynoe.html', context=context)


def zemelnoe_view(request: HttpRequest):
    context = {
        'title': 'Земельное право'
    }
    return render(request, 'homeapp/zemelnoe.html', context=context)


def reputatsii_view(request: HttpRequest):
    context = {
        'title': 'Защита деловой репутации'
    }
    return render(request, 'homeapp/reputatsii.html', context=context)


def konsalting_view(request: HttpRequest):
    context = {
        'title': 'Стратегический консалтинг'
    }
    return render(request, 'homeapp/konsalting.html', context=context)


def meditsinskoe_view(request: HttpRequest):
    context = {
        'title': 'Медицинское право'
    }
    return render(request, 'homeapp/meditsinskoe.html', context=context)


def arbitrazhnaya_view(request: HttpRequest):
    context = {
        'Арбитражная практика'
    }
    return render(request, 'homeapp/arbitrazhnaya.html', context=context)


def sanktsionnaya_view(request: HttpRequest):
    context = {
        'title': 'Санкционная практика'
    }
    return render(request, 'homeapp/sanktsionnaya.html', context=context)


def rabotaem_view(request: HttpRequest):
    context = {
        'title': 'Как мы работаем'
    }
    return render(request, 'homeapp/rabotaem.html', context=context)


def polnomochiya_view(request: HttpRequest):
    context = {
        'title': 'Полномочия адвоката'
    }
    return render(request, 'homeapp/polnomochiya.html', context=context)


def tayna_view(request: HttpRequest):
    context = {
        'title': 'Адвокатская тайна'
    }
    return render(request, 'homeapp/tayna.html', context=context)


def soglashenie_view(request: HttpRequest):
    context = {
        'title': 'Соглашение и ордер'
    }
    return render(request, 'homeapp/soglashenie.html', context=context)


def varianty_view(request: HttpRequest):
    context = {
        'title': 'Варианты вознагрождения'
    }
    return render(request, 'homeapp/varianty.html', context=context)


def case_1(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/cases/1.html', context=context)



def case_2(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_3(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_4(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)



def case_5(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)



def case_6(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_7(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_8(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_9(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_10(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_11(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_12(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_13(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_14(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)


def case_15(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    return render(request, 'homeapp/1.html', context=context)

