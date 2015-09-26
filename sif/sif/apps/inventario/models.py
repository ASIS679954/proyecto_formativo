from django.db import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

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

			(u'Masculinoascu',u'Masculino'),
			(u'Femenino',u'Femenino'),
			(u'Otro',u'Otro'),

		)
	identificacion  = models.CharField(max_length = 20, unique = True)
	nombre 			= models.CharField(max_length=50)
	apellido 		= models.CharField(max_length=50)

	#email			= models.CharField(max_length=30)
	
    #clave 			= models.CharField(max_length=20)
    #estado 		= models.BooleanField(default = True)
    #userito 		= 

	direccion 		= models.CharField(max_length=30)
	telefono 		= models.CharField(max_length=20)
	sexo 			= models.CharField(max_length=15, choices = generos, default = "Masculino")
 	estado 			= models.BooleanField(default = True)

	def __unicode__(self):
		return self.nombre

class Rol(models.Model):

	nombre = models.CharField(max_length=50)
	usuario = models.ForeignKey(Usuario)




	def __unicode__(self):
		return self.nombre

class Proveedor(models.Model):



	identificacion 	= models.CharField(max_length=50, unique = True)
	nombre 			= models.CharField(max_length=50)
	apellido 		= models.CharField(max_length=50)
	telefono 		= models.CharField(max_length=50)
	direccion 		= models.CharField(max_length=50)
	email 			= models.EmailField()
	razon_social 	= models.CharField(max_length=50)


	def __unicode__(self):
		return self.nombre

class CodigoBarras(models.Model):

	codigo 			= models.CharField(max_length=13, unique = True)
	fecha 			= models.DateField(auto_now = True)


	def __unicode__(self):
		return self.codigo

class Producto(models.Model):

	nombre = models.CharField(max_length=50)
	#referencia = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	ancho = models.CharField(max_length=10)
	largo = models.CharField(max_length=10)
	proveedor = models.ForeignKey(Proveedor)
	codigobarras = models.ForeignKey(CodigoBarras)
	valor = models.IntegerField()
	descripcion = models.TextField(max_length=150,blank=True)
	cantidad	= models.IntegerField(default = 0)

	def __unicode__(self):
		return self.nombre



class Sede(models.Model):
	nombre_sede 	= models.CharField(max_length = 30)
	direccion 		= models.CharField(max_length=30)
	telefono 		= models.CharField(max_length=20)

	
	def __unicode__(self):
		return self.nombre_sede


class Salida(models.Model):
	traslados = (

			(u'traslado',u'traslado'),
			(u'cliente',u'cliente'),
			(u'reparacion',u'reparacion'),
		)
	
	codigobarras 	= models.ForeignKey(CodigoBarras)
	descripcion 	= models.TextField(max_length=150,blank=True)
	fecha_salida	= models.DateField(auto_now = True)
	tipo_salida 	= models.CharField(max_length=50,choices = traslados, default = "traslado")
	producto 		= models.ForeignKey(Producto)
	cantidad 		= models.IntegerField()
	sede 			= models.ForeignKey(Sede)
	numero_contrato = models.IntegerField(blank=True,null=True)


	def __unicode__(self):
		return str(self.fecha_salida)




		

class Entrada(models.Model):

	fecha_ingreso	= models.DateField(auto_now = True)
	producto 		= models.ForeignKey(Producto)
	cantidad 		= models.IntegerField()
	observacion		= models.TextField(max_length = 500,blank=True)

	def __unicode__(self):
		return str(self.fecha_ingreso)



