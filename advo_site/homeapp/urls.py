from django.urls import path
from .views import *

app_name = 'homeapp'

urlpatterns = [
    path('', home_index, name='index'),
    path('team/', team_view, name='team'),
    path('cases/', cases_view, name='cases'),
    path('career/', career_view, name='career'),
    path('zashchita-pri-ugolovnom-presledovanii/', zashchita_view, name='zashchita'),
    path('ugolovno-pravovaya-zashchita-biznesa/', business_view, name='business'),
    path('antikorruptsionnyy-komplayns/', antikorruptsionnoe_view, name='antikorruptsionnoe'),
    path('semeynaya-praktikapraktika/', semeynaya_view, name='semeynaya'),
    path('zemelnaya-praktika/', zemelnaya_view, name='zemelnaya'),
    path('nalogovaya-praktika/', nalogovaya_view, name='nalogovaya'),
    path('mediatsiya/', mediatsiya_view, name='mediatsiya'),
    path('it-ip-praktika/', it_ip_praktika_view, name='it-ip-praktika'),
    path('korporativnaya-praktika/', korporativnaya_view, name='korporativnaya'),
    path('meditsinskoe-pravo/', meditsinskoe_view, name='meditsinskoe'),
    path('arbitrazhnaya-praktika/', arbitrazhnaya_view, name='arbitrazhnaya'),
    path('sanktsionnaya-praktika/', sanktsionnaya_view, name='sanktsionnaya'),
    path('kak-my-rabotaem/', rabotaem_view, name='rabotaem'),
    path('polnomochiya-advokata/', polnomochiya_view, name='polnomochiya'),
    path('advokatskaya-tayna/', tayna_view, name='tayna'),
    path('soglashenie-i-order/', soglashenie_view, name='soglashenie'),
    path('varianty-voznagrozhdeniya/', varianty_view, name='varianty'),
    path('cases/1/', case_1, name='case_1'),
    path('cases/2/', case_2, name='case_2'),
    path('cases/3/', case_3, name='case_3'),
    path('cases/4/', case_4, name='case_4'),
    path('cases/5/', case_5, name='case_5'),
    path('cases/6/', case_6, name='case_6'),
    path('cases/7/', case_7, name='case_7'),
    path('cases/8/', case_8, name='case_8'),
    path('cases/9/', case_9, name='case_9'),
    path('cases/10/', case_10, name='case_10'),
    path('cases/11/', case_11, name='case_11'),
    path('cases/12/', case_12, name='case_12'),
    path('cases/13/', case_13, name='case_13'),
    path('cases/14/', case_14, name='case_14'),
    path('cases/15/', case_15, name='case_15'),
    path('privicy/', privicy_view, name='privicy'),
    path('search/<int:page_number>', search_view, name='search'),
    path('download/<path:file_path>', download_resume, name='download'),
    path('news_<slug:slug>/', news_detail, name='news')
]
