from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
	generos = (
			(u'Masculino',u'Masculino'),
			(u'Femenino',u'Femenino'),
			(u'Otro',u'Otro'),

		)
	identificacion  = models.CharField(max_length = 20, unique = True)
	nombre 			= models.CharField(max_length=50)
	apellido 		= models.CharField(max_length=50)
	direccion 		= models.CharField(max_length=30)
	telefono 		= models.CharField(max_length=20)
	sexo 			= models.CharField(max_length=15, choices = generos, default = "Masculino")
	user 			= models.OneToOneField(User)


	def __unicode__(self):
		return self.nombre








