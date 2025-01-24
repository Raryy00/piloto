from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sobre(request):
    return HttpResponse("<h1>Sobre</h1><p>Informações sobre o sistema.</p>")

def contato(request):
    return HttpResponse("<h1>Contato</h1><p>Esta é a página de contato.</p>")

def ajuda(request):
    return HttpResponse("<h1>Ajuda</h1><p>Esta é a página de ajuda.</p>")
