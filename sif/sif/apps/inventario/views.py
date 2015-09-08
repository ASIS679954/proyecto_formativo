# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import FormuCrea
from sif.apps.inventario.models import CodigoBarras
from django.http import HttpResponseRedirect
import barcode

def creaCodigo(request):
	
	informacion = "Inicia"
	if request.method == "POST":
		informacion = "pasa post"
		formulario = FormuCrea(request.POST)
		if formulario.is_valid():
			EAN = barcode.get_barcode_class('ean13')
			ean = EAN(request.POST.get('codigo'))
			ean.save("nuevo")
 			agrega = formulario.save(commit = False)
			agrega.save()
			informacion = "Terminado"
			return HttpResponseRedirect('/codigoBarras/%s' %agrega.id)
	else:
		formulario = FormuCrea()
		ctx = {'form': formulario,'info':informacion}
	return render_to_response('inventario/agregaCB.html',ctx,context_instance = RequestContext(request))
