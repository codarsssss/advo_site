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
    path('ulyanovsk', ulyanovsk_view, name='ulyanovsk'),
    path('privicy/', privicy_view, name='privicy'),
    path('search/<int:page_number>', search_view, name='search'),
    path('download/<path:file_path>', download_resume, name='download'),
    path('individual-service-list/', get_individual_service_list, name='individual_service_list'),
    path('individual-service-list/criminal-defense/', get_criminal_defense_detail, name='criminal_defense'),
    path('individual-service-list/civil-defense/', get_civil_defense_detail, name='civil_defense'),
    path('individual-service-list/inheritance/', get_inheritance_detail, name='inheritance'),
    path('individual-service-list/migration/', get_migration_detail, name='migration'),
    path('individual-service-list/traffic-accident/', get_traffic_accident_detail, name='traffic_accident'),
    path('individual-service-list/license-revocation/', get_license_revocation_detail, name='license_revocation'),
    path('individual-service-list/family-matters/', get_family_matters_detail, name='family_matters'),
    path('individual-service-list/individual-bankruptcy/', get_individual_bankruptcy_detail, name='individual_bankruptcy'),
    path('individual-service-list/consumer-protection/', get_consumer_protection_detail, name='consumer_protection'),
    path('individual-service-list/land-disputes/', get_land_disputes_detail, name='land_disputes'),
    path('individual-service-list/debt-recovery/', get_debt_recovery_detail, name='debt_recovery'),
    path('individual-service-list/medical/', get_medical_detail, name='medical'),
    path('individual-service-list/enforcement-lawyer/', get_enforcement_lawyer_detail, name='enforcement_lawyer'),
    path('individual-service-list/appeals/', get_appeals_detail, name='appeals'),
    path('individual-service-list/administrative-penalties/', get_administrative_penalties_detail, name='administrative_penalties'),
    path('individual-service-list/online-consultation/', get_online_consultation_detail, name='online_consultation'),
    path('legal-service-list/', get_legal_service_list, name='legal_service_list'),
    path('legal-service-list/insolvency-support/', get_insolvecy_support_detail, name='insolvecy_support'),
    path('legal-service-list/complex-support/', get_complex_support_detail, name='complex_support'),
    path('news-list/', get_news_list, name='news_list'),
    path('news_<slug:slug>/', news_detail, name='news_detail'),
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
]
