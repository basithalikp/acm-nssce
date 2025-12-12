# acm_chapter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('events/', views.events_view, name='events'),
    path('our-team/', views.team_view, name='team'),
    path('about/', views.about_view, name='about'),
]