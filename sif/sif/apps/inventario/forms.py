
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
	codigobarras = forms.CharField(widget=forms.TextInput(attrs={'autofocus':''}))
	def clean_codigobarras(self):
		return CodigoBarras.objects.get(codigo=self.cleaned_data['codigobarras'])
	class Meta:
		model = Salida
		exclude = ('producto',)
		
		

		
#Proveedor
class add_prove_form(forms.ModelForm):
	class Meta:
		model = Proveedor

#Producto 
class add_product_form(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ('codigobarras',)

class FormuCrea(forms.ModelForm):
	class Meta:
		model = CodigoBarras
	


    