from django.urls import path
from .views import home_index, about_us_index

app_name = 'homeapp'

urlpatterns = [
    path('', home_index, name='index'),
    path('about-us/', about_us_index, name='about'),
]