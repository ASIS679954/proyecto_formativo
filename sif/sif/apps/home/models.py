from django.db import models
# Create your models here.
class Cliente(models.Model):
	cedula		= models.CharField(max_length = 20, unique = True)
	nombre		= models.CharField(max_length = 20)
	apellido 	= models.CharField(max_length = 20)
	telefono	= models.CharField(max_length = 20)
	direccion	= models.CharField(max_length = 20)
	correo		= models.EmailField()

	def __unicode__ (self):
		return self.nombre	

class Automovil(models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Automovil/%s/%s"%(self.idrefecia, str(filename))
		return ruta

	idrefecia   = models.CharField(max_length = 20, unique = True)
	marca       = models.CharField(max_length = 20)
	modelo		= models.CharField(max_length = 20)
	color		= models.CharField(max_length = 20)
	precio		= models.CharField(max_length = 20)
	status		= models.BooleanField(default = True)
	imagen      = models.ImageField(upload_to = url, null = True,blank = True)

	def __unicode__ (self):
		return self.idrefecia

class Vendedor(models.Model):
	cedula		= models.CharField(max_length = 20, unique = True)
	nombre		= models.CharField(max_length = 20)
	apellido	= models.CharField(max_length = 20)
	telefono	= models.CharField(max_length = 20)
	status		= models.BooleanField(default = True)

	def __unicode__ (self):
		return self.nombre

class Ventas(models.Model):
	idcavtas  	= models.CharField(max_length = 20, unique = True)
	Vendedor	= models.ForeignKey(Vendedor)
	total		= models.DecimalField(max_digits = 20, decimal_places = 2)
	Automovil	= models.ForeignKey(Automovil)
	Cliente		= models.ForeignKey(Cliente)

	def __unicode__ (self):
		return self.idcavtas
