from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
]
