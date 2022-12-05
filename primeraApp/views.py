from django.shortcuts import render
from .models import familia
from django.http import HttpResponse
import datetime
from django.template import Template,context

# Create your views here.
def crearfamilia(request):
    
    mama = familia(nombre="Silvia ",apellido="Mattei ",edad= "1995,6,19")
    papa = familia(nombre ="Marcelo", apellido = "Catini", edad="1996,6,19")
    hermano = familia(nombre = "Mateo", apellido = "Catini", edad = "1999,20,11")
    mama.save()
    papa.save()
    hermano.save()
    cadena=f"   MADRE: Su nombre es {mama.nombre}{mama.apellido} y nacio en {mama.edad}"
    cadena2=f"  PADRE: Su nombre es {papa.nombre}{papa.apellido} y nacio en{papa.edad}"
    cadena3=f"  HERMANO: Su nombre es {hermano.nombre}{hermano.apellido} y nacio en{hermano.edad}"
    cadena4 = f" {cadena}       {cadena2}       {cadena3}"
    return HttpResponse(cadena4)

    

