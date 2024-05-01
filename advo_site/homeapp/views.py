import os
import asyncio
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, FileResponse, Http404
from .forms import ConsultationForm, WorkerForm
from django.contrib import messages

from .models import News, Partner
from .search import search
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
from .notification_bot import send_telegram_message


def download_resume(request, file_path):
    file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_full_path):
        return FileResponse(open(file_full_path, 'rb'))
    raise Http404('Такого файла не существует :(')


def search_form(request, user_input):
    if user_input:
        search_result = search(user_input)
        page_number = request.GET.get('page', 1)
        request.session['search_result'] = search_result
        request.session['title'] = 'Поиск по сайту'
        request.session['page_number'] = page_number
        return redirect(reverse('homeapp:search', args=[page_number]))
    pass


def handle_form(request, form_class):
    form = form_class(request.POST)
    if form.is_valid():
        asyncio.run(send_telegram_message(f'{form.instance.username}-{form.instance.number}'))
        form.save()
        messages.success(request, "Скоро мы с Вами свяжемся для консультации")
        request.session['username'] = request.POST.get('username')
        return True
    else:
        form = form_class()
        return False


def home_index(request: HttpRequest):
    news = News.published.all()  # Все новости, у которых status = Published
    partners = Partner.objects.filter(work_place='moscow')

    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)

    context = {
        'title': 'Главная страница',
        'user': request.session.get('username'),
        'News': news,
        'partners': partners,
    }

    return render(request, 'homeapp/index.html', context=context)


def news_detail(request, slug):
    news_obj = get_object_or_404(News, slug=slug)

    context = {
        'title': 'Новости',
        'news_obj': news_obj
    }

    return render(request, 'homeapp/news_detail.html', context=context)


def team_view(request: HttpRequest):
    partners = Partner.objects.filter(work_place='moscow')
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/team/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)


    context = {
        'title': 'Команда',
        'user': request.session.get('username'),
        'partners': partners,
    }


    return render(request, 'homeapp/team.html', context=context)


def cases_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)

    context = {
        'title': 'Кейсы',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases.html', context=context)


def career_view(request: HttpRequest):
    context = {
        'title': 'Карьера',
        'user': request.session.get('username')
    }

    if request.method == "POST":

        form = WorkerForm(request.POST, request.FILES)
        form_1 = ConsultationForm(request.POST)

        if form.is_valid():
            form.save()
            asyncio.run(send_telegram_message(f'Поступило резюме от {form.instance.fio}'))
            messages.success(request, 'Форма отправленна! Скоро мы с Вами свяжемся')
            return redirect('/career/')

        elif form_1.is_valid():
            form_1.save()
            asyncio.run(send_telegram_message(f'{form_1.instance.username}-{form_1.instance.number}'))
            messages.success(request, 'Мы получили ваш запрос. Скоро перезвоним!')
            return redirect('/career/')

        else:
            # messages.error(request, 'Произошла ошибка. Пожалуйста свяжитесь алтернативными способами')
            form = WorkerForm()
            form_1 = ConsultationForm()

        user_input = request.POST.get('search_input')

        return search_form(request, user_input)

    return render(request, 'homeapp/career.html', context=context)


def zashchita_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/zashchita-pri-ugolovnom-presledovanii/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)



    context = {
        'title': 'Защита при уголовном преследовании',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/zashchita.html', context=context)


def business_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/ugolovno-pravovaya-zashchita-biznesa/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)


    context = {
        'title': 'Уголовно-правовая защита бизнеса',
        'user': request.session.get('username')

    }

    return render(request, 'homeapp/practices/business.html', context=context)


def antikorruptsionnoe_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/korporativnaya/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Антикоррупционный комплайнс',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/korporativnaya.html', context=context)


def semeynaya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/semeynaya-praktikapraktika/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Семейная практика',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/semeynaya.html', context=context)


def zemelnaya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/zemelnaya-praktika/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Земельная практика',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/zemelnaya.html', context=context)


def nalogovaya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/nalogovaya-praktika/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Налоговая практика',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/nalogovaya.html', context=context)


def mediatsiya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/mediatsiya/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Медиация',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/mediatsiya.html', context=context)


def it_ip_praktika_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/it-ip-praktika/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': ' IT/ IP практика',
        'user': request.session.get('username')
    }
    if handle_form(request, ConsultationForm):
        return redirect('/it-ip-praktika/')

    return render(request, 'homeapp/practices/it_ip_praktika.html', context=context)


def korporativnaya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/korporativnaya-praktika/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Корпоративная практика',
        'user': request.session.get('username')
    }
    if handle_form(request, ConsultationForm):
        return redirect('/korporativnaya/')

    return render(request, 'homeapp/practices/korporativnaya.html', context=context)


def meditsinskoe_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/meditsinskoe-pravo/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Медицинское право',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/meditsinskoe.html', context=context)


def arbitrazhnaya_view(request: HttpRequest):
    context = {
        'title': 'Арбитражная практика',
        'user': request.session.get('username')
    }
    if handle_form(request, ConsultationForm):
        return redirect('/arbitrazhnaya-praktika/')

    return render(request, 'homeapp/practices/arbitrazhnaya.html', context=context)


def sanktsionnaya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/sanktsionnaya-praktika/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Санкционная практика',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/practices/sanktsionnaya.html', context=context)


def rabotaem_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/kak-my-rabotaem/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Как мы работаем',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/procedure/rabotaem.html', context=context)


def polnomochiya_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/polnomochiya-advokata/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Полномочия адвоката',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/procedure/polnomochiya.html', context=context)


def tayna_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/advokatskaya-tayna/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Адвокатская тайна',
        'user': request.session.get('username')
    }
    if handle_form(request, ConsultationForm):
        return redirect('/advokatskaya-tayna/')

    return render(request, 'homeapp/procedure/tayna.html', context=context)


def soglashenie_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/soglashenie-i-order/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Соглашение и ордер',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/procedure/soglashenie.html', context=context)


def varianty_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/varianty-voznagrozhdeniya/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Варианты вознагрождения',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/procedure/varianty.html', context=context)


def case_1(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/1/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Оправдательный приговор',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/1.html', context=context)

def case_2(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/2/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Особо тяжкое преступление',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/2.html', context=context)


def case_3(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/3/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Оправдательный приговор мошенничество, легализация',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/3.html', context=context)


def case_4(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/4/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Получение взятки',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/4.html', context=context)



def case_5(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/5/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Вердикт присяжных заседателей не виновен в убийстве',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/5.html', context=context)


def case_6(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/6/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'ч. 4 ст. 159 УК РФ',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/6.html', context=context)


def case_7(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/7/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Хищение сотрудником на рабочем месте',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/7.html', context=context)


def case_8(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/8/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Банкротство физических лиц',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/8.html', context=context)


def case_9(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/9/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Потерпевшие ч. 4 ст. 159 УК РФ',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/9.html', context=context)


def case_10(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/10/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Особо тяжкое преступление',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/10.html', context=context)


def case_11(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/11/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Деловая репутация',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/11.html', context=context)


def case_12(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/12/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Злоупотребление должностными полномочиями',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/12.html', context=context)


def case_13(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/13/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Превышение должностных полномочий-компромисс',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/13.html', context=context)


def case_14(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/14/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Застройщик',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/14.html', context=context)


def case_15(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/cases/15/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Суд отклонил незаконные требования прокуратуры',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/cases/15.html', context=context)


def privicy_view(request: HttpRequest):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/privicy/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)
    context = {
        'title': 'Политика конфиденциальности',
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/privicy.html', context=context)


def search_view(request: HttpRequest, page_number):
    search_result = request.session.get('search_result')
    paginator = Paginator(search_result, 10)
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/search/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)

    context = {
        'title': 'Поиск по сайту',
        'results': search_result,
        'page_obj': page_obj,
        'user': request.session.get('username')
    }

    return render(request, 'homeapp/search.html', context=context)


def ulyanovsk_view(request: HttpRequest):
    partners = Partner.objects.filter(work_place='ulyanovsk')
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/team/')
        user_input = request.POST.get('search_input')
        return search_form(request, user_input)

    context = {
        'title': 'Ульяновск',
        'user': request.session.get('username'),
        'partners': partners,
    }

    return render(request, 'homeapp/filials/ulyanovsk.html', context=context)