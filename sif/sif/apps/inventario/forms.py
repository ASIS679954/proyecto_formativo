from django import forms

class FormuCrea(forms.Form):
	codigo = models.CharField(label = 'Codigo' , max_length=13)
	fecha = models.DateField(label = 'Fecha', auto_now = True)
