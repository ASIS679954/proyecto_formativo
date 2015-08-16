
from django.db import models

class Usuario(models.Model):
	genero = (
		   (u'M',u'masculino'),
		   (u'F',u'femenino'),
		   (u'Otro',u'otro'),
		)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	telefono = models.CharField(max_length=20)
	sexo = models.CharField(max_length=15, choices = genero)

	def __unicode__(self):
		return self.nombre


class Rol(models.Model):
	nombre = models.CharField(max_length=50)
	usuario = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	ancho = models.CharField(max_length=10)
	largo = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nombre

class Departamento(models.Model):
	nombre = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.nombre	

class Municipio(models.Model):
	nombre = models.CharField(max_length=50)
	departamento = models.ForeignKey(Departamento)


	def __unicode__(self):
		return self.nombre			


class Proveedor(models.Model):
	identificacion = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	municipio = models.ForeignKey(Municipio)
	producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return self.identificacion


class Transferencia(models.Model):
	fecha_transferencia = models.DateField()



	def __unicode__(self):
		return str(self.fecha_transferencia)


class Sede(models.Model):
	municipio = models.ForeignKey(Municipio)
	direccion = models.CharField(max_length=30)
	telefono = models.CharField(max_length=20)
	producto = models.ForeignKey(Producto)
	transferencia = models.DateField(
)	#usuario = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.municipio.nombre



class CodigoBarras(models.Model):
	codigo = models.CharField(max_length=13)
	fecha = models.DateField()

	def __unicode__(self):
		return self.codigo





		
