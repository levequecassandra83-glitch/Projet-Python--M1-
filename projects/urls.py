from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_projects, name='liste_projects'),
    path('<int:pk>/', views.detail_project, name='detail_project'),
]
