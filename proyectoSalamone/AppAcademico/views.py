

from django.shortcuts import render, redirect
from .models import Curso, Carrera, Estudiante
# Create your views here.


def home(request):
    return render(request, "home.html")



def gestionCursos (request):
    
    cursosListados=Curso.objects.all()
    return render (request, "gestionCursos.html", {"cursos": cursosListados})


def registrarCurso (request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']
    docente=request.POST['txtDocente']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, docente=docente)
    return redirect('/gestionCursos/')

def edicionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render (request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito'] 
    docente=request.POST['txtDocente']   

    curso=Curso.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.creditos=creditos
    curso.docente=docente
    curso.save()
    return redirect('/gestionCursos/')


def eliminarCurso (request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect ('/gestionCursos/')





def carreras (request):
    carreras=Carrera.objects.all()
    return render (request, "carreras.html", {"carreras": carreras})


def registrarCarrera (request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    duracion=request.POST['numDuracion']
   

    carreras=Carrera.objects.create(codigo=codigo, nombre=nombre, duracion=duracion)
    return redirect('/carreras/')

def edicionCarrera(request, codigo):
    carrera=Carrera.objects.get(codigo=codigo)
    return render (request, "edicionCarrera.html", {"carrera":carrera})

def editarCarrera(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    duracion=request.POST['numDuracion'] 
   

    carrera=Carrera.objects.get(codigo=codigo)
    carrera.nombre=nombre
    carrera.duracion=duracion
    carrera.save()
    return redirect('/carreras/')


def eliminarCarrera (request, codigo):
    carrera=Carrera.objects.get(codigo=codigo)
    carrera.delete()
    return redirect('/carreras/')





def estudiantes (request):
    
    estudiantes=Estudiante.objects.all()
    return render (request, "estudiantes.html", {"estudiantes": estudiantes})


def registrarEstudiante (request):
   
    apellidoPaterno=request.POST['txtApePaterno']
    apellidoMaterno=request.POST['txtApeMaterno']
    nombres=request.POST['txtNombres']
    fechaNacimiento=request.POST['txtFecha']

    estudiantes=Estudiante.objects.create( apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno, nombres=nombres, fechaNacimiento=fechaNacimiento )
    estudiantes.save()
    return redirect('/estudiantes/')

# def edicionEstudiante(request,):
#     estudiante=Estudiante.objects.get(id=id)
#     return render (request, "edicionEstudiante.html", {"estudiante":estudiante})

# def editarEstudiante(request):
#     id=request.POST['txtId']
#     apellidoPaterno=request.POST['txtApePaterno']
#     apellidoMaterno=request.POST['txtApeMaterno']
#     nombres=request.POST['txtNombres']
#     fechaNacimiento=request.POST['txtFecha']

#     estudiante=Estudiante.objects.get(id=id)
#     estudiante.id=id
#     estudiante.apellidoPaterno=apellidoPaterno
#     estudiante.apellidoMaterno=apellidoMaterno
#     estudiante.nombres=nombres
#     estudiante.fechaNacimiento=fechaNacimiento
#     estudiante.save()
#     return redirect('/estudiantes/')


def eliminarEstudiante (request, id):
    estudiante=Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect ('/estudiantes/')


# def estudiante (request):
#     return redirect ('/estudiantes/')

def buscar(request):
   
    if request.GET['txtApePaterno']:
        apellidoPaterno=request.GET['txtApePaterno']
        estudiantes=Estudiante.objects.filter(apellidoPaterno__icontains=apellidoPaterno)
        return render(request, 'resultadoBusqueda.html', {'estudiantes':estudiantes, 'apellidoPaterno': apellidoPaterno})

    else:
        respuesta= "No se ingresaste ningún Apellido"
        # return HttpResponse(respuesta)  
        return render(request, 'resultadoBusqueda.html', {'respuesta': respuesta})
        