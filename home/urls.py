from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('contato/', views.contato, name='contato'),  # Página de contato
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('local/', views.local, name='local'),
    path('exibiritem/<int:id>/', views.exibiritem, name='exibiritem'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('dia/<int:num>/', views.dia_da_semana, name='dia_da_semana'),
]
