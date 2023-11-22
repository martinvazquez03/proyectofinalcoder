# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def view_cursos(request):
    #return render(request,"templates/AppCoder/padre.html")
    nom = "martin"
    ap = "vazquez perez"
    ahora = datetime.now()
    diccionario = {"nombre": nom, "apellido": ap, "nacionalidad":"argentino","hora": ahora, "ciudades": ['lima', 'san pablo']}
    return render(request,"AppCoder/padre.html",context=diccionario)
        

def view_inicio(xx):
    return HttpResponse("bienvenidos!!!!!!!!!!!!!")