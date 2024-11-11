from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.ajouter_personne, name='ajouter_personne'),
]
