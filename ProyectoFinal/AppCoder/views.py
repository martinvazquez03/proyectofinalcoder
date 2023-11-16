from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.urls import view_cursos,view_inicio
# Create your views here.

def view_inicio(request):
    return HttpResponse("bienvenidos!!!!!!!!!!!!!")

def view_cursos(request):
    return render(request,"templates/AppCoder/padre.html")