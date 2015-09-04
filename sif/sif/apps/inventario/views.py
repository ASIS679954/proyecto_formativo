# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import FormuCrea
from sif.apps.inventario.models import CodigoBarras
from django.http import HttpResponseRedirect


def creaCodigo(request):

	if request.method == 'POST': 
		form = FormuCrea(request.POST)
		if form.is_valid():
            agrega = formulario.save(commit = False)
            agrega.save()
			return HttpResponseRedirect('/codigoBarras/%s' %agrega.id)
	else:
		form = FormuCrea()
	return render_to_response(request, 'inventario/agregaCB.html',{'form': form},context_instance = RequestContext(request))
