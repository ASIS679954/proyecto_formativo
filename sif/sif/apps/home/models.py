from django.db import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class Departamento(models.Model):
	nombre 		= models.CharField(max_length=50)
	municipio 	= models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Usuario(models.Model):
	generos = (
			(u'mascu',u'Masculino'),
			(u'feme',u'Femenino'),
			(u'otro',u'Otro'),
		)
	identificacion  = models.CharField(max_length = 20, unique = True)
	nombre 			= models.CharField(max_length=50)
	apellido 		= models.CharField(max_length=50)
	#email			= models.CharField(max_length=30)
	direccion 		= models.CharField(max_length=30)
	telefono 		= models.CharField(max_length=20)
	sexo 			= models.CharField(max_length=15, choices = generos, default = "Masculino")
    #clave 			= models.CharField(max_length=20)
    #estado 		= models.BooleanField(default = True)
    #userito 		= 
	def __unicode__(self):
		return self.nombre

class Rol(models.Model):
	nombre = models.CharField(max_length=50)
	usuario = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.nombre

class Proveedor(models.Model):
	identificacion = models.CharField(max_length=50, unique = True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	email = models.EmailField()
	razon_social = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class CodigoBarras(models.Model):
	codigo = models.CharField(max_length=13)
	fecha = models.DateField(auto_now = True)

	def __unicode__(self):
		return self.codigo

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	referencia = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	ancho = models.CharField(max_length=10)
	largo = models.CharField(max_length=10)
	proveedor = models.ForeignKey(Proveedor)
	codigobarras = models.ForeignKey(CodigoBarras)
	valor = models.IntegerField()
	descripcion = models.TextField(max_length=150)
	cantidad	= models.IntegerField(default = 0)

	def __unicode__(self):
		return self.nombre

class Sede(models.Model):
	nombre_sede = models.CharField(max_length = 30)
	direccion = models.CharField(max_length=30)
	telefono = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.nombre_sede

class Salida(models.Model):
	fecha_salida = models.DateField(auto_now = True)
	tipo_salida = models.CharField(max_length=50)
	codigobarras = models.ForeignKey(CodigoBarras)
	cantidad = models.IntegerField()


	def __unicode__(self):
		return str(self.fecha_salida)



		
