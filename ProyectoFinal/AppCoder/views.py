# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.urls import view_cursos, view_inicio

def view_cursos(request):
    return render(request,"templates/AppCoder/padre.html")

def view_inicio(xx):
    return HttpResponse("bienvenidos!!!!!!!!!!!!!")