<<<<<<< HEAD

from django import forms
from sif.apps.inventario.models import CodigoBarras
=======

from sif.apps.inventario.models import *
from django import forms





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
		model = Producto
		exclude = ('codigobarras',)
		''' 
		widgets = {
			'codigobarras': forms.HiddenInput(attrs={'value':'1234'}),
		}
		'''
>>>>>>> origin/esteban
class FormuCrea(forms.ModelForm):
	class Meta:
		model = CodigoBarras
	

<<<<<<< HEAD
	


=======

    
>>>>>>> origin/esteban
