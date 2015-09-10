from sif.apps.inventario.models import *
from django import forms

opciones_report = (
    ('entrada', 'Reporte Por Entrada'),
    ('salida', 'Reporte Por Salida'),
    
)


class busqueda_form(forms.Form):

	fecha_inicio = forms.CharField(widget = forms.TextInput())
	fecha_fin = forms.CharField(widget = forms.TextInput())
	opcion = forms.ChoiceField(choices=opciones_report)