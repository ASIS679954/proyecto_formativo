from django import forms
from sif.apps.inventario.models import *



#Sede
class add_sede_form(forms.ModelForm):
	class Meta:
		model   = Sede

#Entrada
class add_entrada_form(forms.ModelForm):
	codigobarras = forms.CharField(widget=forms.TextInput(attrs={'autofocus':''}))
	def clean_codigobarras(self):
		return CodigoBarras.objects.get(codigo=self.cleaned_data['codigobarras'])
	class Meta:
		model 	= Entrada
		exclude = ('producto','fecha_ingreso')
		fields = ['codigobarras','cantidad','observacion','referencia']
		
#Salida
class add_salida_form(forms.ModelForm):
	codigobarras = forms.CharField(widget=forms.TextInput(attrs={'autofocus':''}))
	def clean_codigobarras(self):
		return CodigoBarras.objects.get(codigo=self.cleaned_data['codigobarras'])
	def clean_numero_contrato(self):
		tipo = self.cleaned_data['tipo_salida']
		contrato = self.cleaned_data['numero_contrato']
		if "cliente" in tipo:
			if not contrato:
				raise forms.ValidationError(
					"Tienes que especificar el numero del contrato"
				)

		return contrato
	class Meta:
		model = Salida
		exclude = ('producto',)
		fields = ['codigobarras','cantidad','tipo_salida','numero_contrato','sede','descripcion']

		
		
#Proveedor
class add_prove_form(forms.ModelForm):
	class Meta:
		model = Proveedor

#Producto 
class add_product_form(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ('codigobarras','estado')
		


class FormuCrea(forms.ModelForm):
	class Meta:
		model = CodigoBarras
	
