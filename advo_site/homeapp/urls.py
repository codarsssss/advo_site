from django.urls import path
from .views import *

app_name = 'homeapp'

urlpatterns = [
    path('', home_index, name='index'),
    path('team/', team_view, name='team'),
    path('cases/', cases_view, name='cases'),
    path('career/', career_view, name='career'),
    path('about-us/', about_view, name='about'),
    path('zashchita-pri-ugolovnom-presledovanii/', zashchita_view, name='zashchita'),
    path('ugolovno-pravovaya-zashchita-biznesa/', business_view, name='business'),
    path('antikorruptsionnoe-prosveshchenie/', antikorruptsionnoe_view, name='antikorruptsionnoe'),
    path('semeynoe-pravo/', semeynoe_view, name='semeynoe'),
    path('zemelnoe-pravo /', zemelnoe_view, name='zemelnoe'),
    path('zashchita-delovoy-reputatsii/', reputatsii_view, name='reputatsii'),
    path('strategicheskiy-konsalting/', konsalting_view, name='konsalting'),
    path('meditsinskoe-pravo/', meditsinskoe_view, name='meditsinskoe'),
    path('arbitrazhnaya-praktika/', arbitrazhnaya_view, name='arbitrazhnaya'),
    path('sanktsionnaya-praktika/', sanktsionnaya_view, name='sanktsionnaya'),
    path('kak-my-rabotaem/', rabotaem_view, name='rabotaem'),
    path('polnomochiya-advokata/', polnomochiya_view, name='polnomochiya'),
    path('advokatskaya-tayna/', tayna_view, name='tayna'),
    path('soglashenie-i-order/', soglashenie_view, name='soglashenie'),
    path('varianty-voznagrozhdeniya/', varianty_view, name='varianty'),
    path('cases/1', case_1, name='case_1'),
    path('cases/1', case_2, name='case_2'),
    path('cases/1', case_3, name='case_3'),
    path('cases/1', case_4, name='case_4'),
    path('cases/1', case_5, name='case_5'),
    path('cases/1', case_6, name='case_6'),
    path('cases/1', case_7, name='case_7'),
    path('cases/1', case_8, name='case_8'),
    path('cases/1', case_9, name='case_9'),
    path('cases/1', case_10, name='case_10'),
    path('cases/1', case_11, name='case_11'),
    path('cases/1', case_12, name='case_12'),
    path('cases/1', case_13, name='case_13'),
    path('cases/1', case_14, name='case_14'),
    path('cases/1', case_15, name='case_15'),
]
