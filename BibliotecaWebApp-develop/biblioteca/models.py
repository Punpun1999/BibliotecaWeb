from django.db import models
from datetime import date

class Autor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    nacionalidad=models.CharField(max_length=60)
    activo=models.BooleanField(default=True)

class Libro(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)
    isbn=models.IntegerField()
    autor=models.ForeignKey(Autor,related_name="libros",on_delete=models.CASCADE)
    activo=models.BooleanField(default=True)

class Socio(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField(default=date.today)
    activo=models.BooleanField(default=True)

class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    numero_legajo=models.CharField(max_length=30)
    activo=models.BooleanField(default=True)



