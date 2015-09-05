from sif.apps.inventario.models import *
from django import forms

class add_sede_form(forms.ModelForm):
	class Meta:
		model   = Sede
	

