from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('apropos/', views.apropos, name='apropos'),
    path('journal/', views.journal, name='journal'),
]
