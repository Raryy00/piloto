# home/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def local(request):
    return render(request, 'local.html')

def exibiritem(request, id):
    return render(request, 'exibiritem.html', {'id': id})
