from sif.apps.inventario.models import *
from django import forms

class busqueda_form(forms.Form):

	fecha_inicio = forms.CharField(widget = forms.TextInput())
	fecha_fin = forms.CharField(widget = forms.TextInput())
	