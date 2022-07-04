from django.shortcuts import render
from django.http import HttpResponse
from mvt_app.models import Familia

def familia(request):
    context= {}
    context["familiares"]= Familia.objects.all()
    
    return render(request,'mvt_app/familia.html', context)

def mostrar_edad(request):
    context= {}
    context["edades"]= Familia.objects.edad()

    return render(request,'mvt_app/edad.html', context)

def mostrar_nombre(request):
    context= {}
    context["nombres"]= Familia.objects.nombre()

    return render(request, 'mvt_app/nombre.html', context)   
