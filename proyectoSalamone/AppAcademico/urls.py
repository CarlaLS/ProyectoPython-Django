from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    
    path('carreras/', carreras, name='carreras'),
    path('registrarCarrera/', registrarCarrera, name='registrarCarrera'),
    path('edicionCarrera/<codigo>', edicionCarrera, name='edicionCarrera'),
    path('editarCarrera/', editarCarrera, name='editarCarrera'),
    path('eliminarCarrera/<codigo>', eliminarCarrera, name='eliminarCarrera'),
    
    path('gestionCursos/', gestionCursos, name='gestionCursos'),
    path('registrarCurso/', registrarCurso, name='registrarCurso'),
    path('edicionCurso/<codigo>', edicionCurso, name='edicionCurso'),
    path('editarCurso/', editarCurso, name='editarCurso'),
    path('eliminarCurso/<codigo>', eliminarCurso, name='eliminarCurso'),


    path('estudiantes/', estudiantes, name='estudiantes'),
    path('registrarEstudiante/', registrarEstudiante, name='registrarEstudiante'),
    # path('edicionEstudiante/<id>', edicionEstudiante, name='edicionEstudiante'),
    # path('editarEstudiante/', editarEstudiante, name='editarEstudiante'),
    
    path('eliminarEstudiante/<id>', eliminarEstudiante, name='eliminarEstudiante'),
    path('buscar/', buscar, name='buscar'),
]
