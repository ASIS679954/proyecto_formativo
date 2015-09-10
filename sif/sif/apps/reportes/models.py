from django.db import models

# Create your models here.
class Producto(models.Model):
	
	def __unicode__(self):
		return self.nombre