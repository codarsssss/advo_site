from django.urls import path
from .views import home_index

app_name = 'homeapp'

urlpatterns = [
    path('', home_index, name='index'),
]