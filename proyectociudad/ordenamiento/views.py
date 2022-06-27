from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *
from ordenamiento.forms import *

# importar los formularios de forms.py 


def index(request):
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    informacion_template = {'barrios':barrios,'parroquias': parroquias, 'numParroquias': len(parroquias),'numBarrios': len(barrios)}
    return render(request, 'index.html', informacion_template)


def listarBarrio(request):    
    barrios = Barrio.objects.all()   
    informacion_template = {'barrios': barrios,  'numBarrios' : len(barrios)}
    return render(request, 'listadoBarrios.html', informacion_template)


def crearParroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)


def crearBarrioParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrioParroquia.html', diccionario)

def editarParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'editarParroquia.html', diccionario)

def editarBarrio(request, id):
    barrio =Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario,'barrio': barrio}

    return render(request, 'editarBarrio.html', diccionario) 