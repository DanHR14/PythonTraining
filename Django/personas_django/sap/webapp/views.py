from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedida(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Dàniel, 6654787565')