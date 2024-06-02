from django.urls import path
from .views import *
app_name = 'sitepages'

urlpatterns =[
    path('',Home,name='homepage'),
    path('about/',About,name='aboutpage'),
    path('weekly-grand-prize/',Weekly_prize,name='weeklygrandprize'),
    path('contact/',Contact,name='contactpage'),
    path('prize/<int:prize_id>/', prize_detail, name='prize_detail'),
    path('enter/<int:prize_id>/',enter_to_win, name='enter_to_win'),
    path('entry_success/<int:entry_id>/',entry_success, name='entry_success'),
]