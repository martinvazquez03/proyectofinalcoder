from django.urls import path
from AppCoder.views import view_cursos, view_inicio

urlpatterns = [
    path('inicio/',view_inicio),
    path('cursos/',view_cursos)
]
