# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def view_cursos(request):
    #return render(request,"templates/AppCoder/padre.html")
    nom = "martin"
    ap = "vazquez perez"
    ruta = r"C:\Users\josem\OneDrive\Escritorio\proyecto final\ProyectoFinal\AppCoder\templates\AppCoder\padre.html"
    diccionario = {"nombre": nom, "apellido": ap}
    mi_archivo = open(ruta,"r",encoding="utf-8")
    plantilla = Template(mi_archivo.read())
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
        

def view_inicio(xx):
    return HttpResponse("bienvenidos!!!!!!!!!!!!!")