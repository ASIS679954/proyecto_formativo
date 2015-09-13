from sif.apps.inventario.models import *
from django import forms

class FormuCrea(forms.Form):
	codigo = models.CharField(label = 'Codigo' , max_length=13)
	fecha = models.DateField(label = 'Fecha', auto_now = True)
	



#Sede
class add_sede_form(forms.ModelForm):
	class Meta:
		model   = Sede

#Entrada
class add_entrada_form(forms.ModelForm):
	class Meta:
		model 	= Entrada
	
#Operador
class add_operador_form(forms.ModelForm):
	class Meta:
		model  = Usuario
		exclude= {'estado'}

#Salida
class add_salida_form(forms.ModelForm):
	class Meta:
		model = Salida

#Proveedor
class add_prove_form(forms.ModelForm):
	class Meta:
		model = Proveedor

#Producto 
class add_product_form(forms.ModelForm):
	class Meta:
		model  = Producto

