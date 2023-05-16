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
]
