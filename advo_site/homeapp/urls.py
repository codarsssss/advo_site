from django.urls import path
from .views import *

app_name = 'homeapp'

urlpatterns = [
    path('', home_index, name='index'),
    path('team/', team_view, name='team'),
    path('cases/', cases_view, name='cases'),
    path('career/', career_view, name='career'),
    path('about-us/', about_view, name='about'),
]
