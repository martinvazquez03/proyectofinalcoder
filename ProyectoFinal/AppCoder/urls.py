from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def view_cursos(request):
    return render(request,"AppCoder/padre.html")

def view_inicio(xx):
    return HttpResponse("bienvenidos!!!!!!!!!!!!!")

urlpatterns = [
    path('inicio/',view_inicio),
    path('cursos/',view_cursos)
]
