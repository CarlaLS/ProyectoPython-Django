from django.db import models

# Create your models here.

class Carrera (models.Model):
    codigo= models.CharField(max_length=3)
    nombre=models.CharField(max_length=50)
    duracion=models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt="{0} (Duración: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante (models.Model):
    apellidoPaterno=models.CharField(max_length=35)
    apellidoMaterno=models.CharField(max_length=35)
    nombres=models.CharField(max_length=35)
    fechaNacimiento=models.DateField()

    # sexos =[
    #     ('F', 'Femenino'),
    #     ('M', 'Masculino')
    # ]
    # sexo=models.CharField(max_length=1, choices=sexos, default='F')


    def __str__(self):
        txt="{0} {1}, {2}"
        return txt.format (self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
  
class Curso (models.Model):
    codigo=models.CharField(max_length=6)
    nombre=models.CharField(max_length=30)
    creditos=models.PositiveSmallIntegerField()
    docente=models.CharField(max_length=100)
    
    def __str__(self):
        texto= "{0} ({1}) / Docente: {2}"
        return texto.format(self.nombre, self.creditos, self.docente)


