from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    num_personas = Persona.objects.count()
    personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'num_personas': num_personas, 'personas': personas})

