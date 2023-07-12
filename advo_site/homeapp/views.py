from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ConsultationForm, WorkerForm
from django.contrib import messages


def handle_form(request, form_class):
    form = form_class(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "DONE!")
            return True
        else:
            form = form_class()
            messages.error(request, "DONE!")
            return False


def home_index(request: HttpRequest):
    context = {
        'title': 'Главная страница'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/')

    return render(request, 'homeapp/index.html', context=context)


def team_view(request: HttpRequest):
    context = {
        'title': 'Команда'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/team/')

    return render(request, 'homeapp/team.html', context=context)


def cases_view(request: HttpRequest):
    context = {
        'title': 'Кейсы'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/')
    return render(request, 'homeapp/cases.html', context=context)


def career_view(request: HttpRequest):
    context = {
        'title': 'Карьера'
    }

    if request.method == "POST":

        form = WorkerForm(request.POST, request.FILES)
        form_1 = ConsultationForm(request.POST)


        if form.is_valid():
            form.save()
            messages.success(request, 'Мы получили ваш запрос. Скоро перезвоним!')
            return redirect('/career/')

        elif form_1.is_valid():
            form_1.save()
            messages.success(request, 'Мы получили ваш запрос. Скоро перезвоним!')
            return redirect('/career/')

        else:
            messages.error(request, 'Произошла ошибка. Пожалуйста свяжитесь алтернативными способами')
            form = WorkerForm()
            form_1 = ConsultationForm()

    return render(request, 'homeapp/career.html', context=context)


def zashchita_view(request: HttpRequest):
    context = {
        'title': 'Защита при уголовном преследовании'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/zashcita/')
    return render(request, 'homeapp/practices/zashchita.html', context=context)


def business_view(request: HttpRequest):
    context = {
        'title': 'Уголовно-правовая защита бизнеса'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/business/')
    return render(request, 'homeapp/practices/business.html', context=context)


def antikorruptsionnoe_view(request: HttpRequest):
    context = {
        'title': 'Антикоррупционный комплайнс'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/korporativnaya/')
    return render(request, 'homeapp/practices/korporativnaya.html', context=context)


def semeynaya_view(request: HttpRequest):
    context = {
        'title': 'Семейная практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/semeynaya/')
    return render(request, 'homeapp/practices/semeynaya.html', context=context)


def zemelnaya_view(request: HttpRequest):
    context = {
        'title': 'Земельная практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/zemelnaya/')
    return render(request, 'homeapp/practices/zemelnaya.html', context=context)


def nalogovaya_view(request: HttpRequest):
    context = {
        'title': 'Налоговая практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/nalogovaya/')
    return render(request, 'homeapp/practices/nalogovaya.html', context=context)


def mediatsiya_view(request: HttpRequest):
    context = {
        'title': 'Медиация'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/mediatsiya/')
    return render(request, 'homeapp/practices/mediatsiya.html', context=context)


def it_ip_praktika_view(request: HttpRequest):
    context = {
        'title': ' IT/ IP практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/it-ip-praktika/')
    return render(request, 'homeapp/practices/it_ip_praktika.html', context=context)


def korporativnaya_view(request: HttpRequest):
    context = {
        'title': 'Корпоративная практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/korporativnaya/')
    return render(request, 'homeapp/practices/korporativnaya.html', context=context)


def meditsinskoe_view(request: HttpRequest):
    context = {
        'title': 'Медицинское право'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/meditsinskoe/')
    return render(request, 'homeapp/practices/meditsinskoe.html', context=context)


def arbitrazhnaya_view(request: HttpRequest):
    context = {
        'title': 'Арбитражная практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/arbitrazhnaya/')
    return render(request, 'homeapp/practices/arbitrazhnaya.html', context=context)


def sanktsionnaya_view(request: HttpRequest):
    context = {
        'title': 'Санкционная практика'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/sanktsionnaya/')
    return render(request, 'homeapp/practices/sanktsionnaya.html', context=context)


def rabotaem_view(request: HttpRequest):
    context = {
        'title': 'Как мы работаем'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/rabotaem/')
    return render(request, 'homeapp/procedure/rabotaem.html', context=context)


def polnomochiya_view(request: HttpRequest):
    context = {
        'title': 'Полномочия адвоката'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/polnomochiya/')
    return render(request, 'homeapp/procedure/polnomochiya.html', context=context)


def tayna_view(request: HttpRequest):
    context = {
        'title': 'Адвокатская тайна'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/tayna/')
    return render(request, 'homeapp/procedure/tayna.html', context=context)


def soglashenie_view(request: HttpRequest):
    context = {
        'title': 'Соглашение и ордер'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/soglashenie/')
    return render(request, 'homeapp/procedure/soglashenie.html', context=context)


def varianty_view(request: HttpRequest):
    context = {
        'title': 'Варианты вознагрождения'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/varianty/')
    return render(request, 'homeapp/procedure/varianty.html', context=context)


def case_1(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/1/')
    return render(request, 'homeapp/cases/1.html', context=context)

def case_2(request: HttpRequest):
    context = {
        'title': 'Особо тяжкое преступление'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/2/')
    return render(request, 'homeapp/cases/2.html', context=context)


def case_3(request: HttpRequest):
    context = {
        'title': 'Оправдательный приговор мошенничество, легализация'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/3/')
    return render(request, 'homeapp/cases/3.html', context=context)


def case_4(request: HttpRequest):
    context = {
        'title': 'Получение взятки'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/4/')
    return render(request, 'homeapp/cases/4.html', context=context)



def case_5(request: HttpRequest):
    context = {
        'title': 'Вердикт присяжных заседателей не виновен в убийстве'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/5/')
    return render(request, 'homeapp/cases/5.html', context=context)



def case_6(request: HttpRequest):
    context = {
        'title': 'ч. 4 ст. 159 УК РФ'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/6/')
    return render(request, 'homeapp/cases/6.html', context=context)


def case_7(request: HttpRequest):
    context = {
        'title': 'Хищение сотрудником на рабочем месте'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/7/')
    return render(request, 'homeapp/cases/7.html', context=context)


def case_8(request: HttpRequest):
    context = {
        'title': 'Банкротство физических лиц'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/8/')
    return render(request, 'homeapp/cases/8.html', context=context)


def case_9(request: HttpRequest):
    context = {
        'title': 'Потерпевшие ч. 4 ст. 159 УК РФ'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/9/')
    return render(request, 'homeapp/cases/9.html', context=context)


def case_10(request: HttpRequest):
    context = {
        'title': 'Особо тяжкое преступление'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/10/')
    return render(request, 'homeapp/cases/10.html', context=context)


def case_11(request: HttpRequest):
    context = {
        'title': 'Деловая репутация'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/11/')
    return render(request, 'homeapp/cases/11.html', context=context)


def case_12(request: HttpRequest):
    context = {
        'title': 'Злоупотребление должностными полномочиями'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/12/')
    return render(request, 'homeapp/cases/12.html', context=context)


def case_13(request: HttpRequest):
    context = {
        'title': 'Превышение должностных полномочий-компромисс'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/13/')
    return render(request, 'homeapp/cases/13.html', context=context)


def case_14(request: HttpRequest):
    context = {
        'title': 'Застройщик'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/14/')
    return render(request, 'homeapp/cases/14.html', context=context)


def case_15(request: HttpRequest):
    context = {
        'title': 'Суд отклонил незаконные требования прокуратуры'
    }
    if handle_form(request, ConsultationForm):
        return redirect('/cases/15/')
    return render(request, 'homeapp/cases/15.html', context=context)
