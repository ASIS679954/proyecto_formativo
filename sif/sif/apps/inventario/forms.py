from django import forms
from sif.apps.inventario.models import CodigoBarras
class FormuCrea(forms.ModelForm):
	class Meta:
		model = CodigoBarras
	
