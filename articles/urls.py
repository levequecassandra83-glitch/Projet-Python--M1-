from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('<int:pk>/', views.detail_article, name='detail_article'),
]
