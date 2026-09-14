from django.urls import path
from . import views

urlpatterns = [
    path('', views.themen_liste, name='themen_liste'),
    path('thema/<int:thema_id>/', views.thema_detail, name='thema_detail'),
    #TODO Add URL for editing an existing topic
    
]