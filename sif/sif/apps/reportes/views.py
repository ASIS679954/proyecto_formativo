from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.reportes.forms import *
from sif.apps.inventario.models import *
from django.http import HttpResponseRedirect



def busqueda_view(request): 
	if request.method == 'POST':
		formulario = busqueda_form(request.POST)
		if formulario.is_valid():
			fecha_inicio = formulario.cleaned_data['fecha_inicio']
			fecha_fin = formulario.cleaned_data['fecha_fin']
			opci = formulario.cleaned_data['opcion']
			if opci == "entrada":
				lista_reporte = Entrada.objects.filter(fecha_ingreso__range=[fecha_inicio, fecha_fin])

				ctx = {'reporte' : lista_reporte,'form': formulario, 'opc' : opci}
				return render_to_response('reportes/reportes.html',ctx, context_instance = RequestContext(request))
			else:
				lista_reporte = Salida.objects.filter(fecha_salida__range=[fecha_inicio, fecha_fin])
				ctx = {'reporte' : lista_reporte,'form': formulario, 'opc' : opci}
				return render_to_response('reportes/reportes.html',ctx, context_instance = RequestContext(request))	

	else:
		formulario = busqueda_form()
	ctx = {'form': formulario}
	return render_to_response('reportes/reportes.html',ctx , context_instance=RequestContext(request))
