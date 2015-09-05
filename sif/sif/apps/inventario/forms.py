from django import forms
from sif.apps.inventario.models import Producto


class add_product_form(forms.ModelForm):
	class Meta:
		model  = Producto

		