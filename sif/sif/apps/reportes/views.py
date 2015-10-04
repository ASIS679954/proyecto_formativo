from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.reportes.forms import *
from sif.apps.inventario.models import *
from django.http import HttpResponseRedirect

#lista reportes
def reportes_view(request):
	return render_to_response('reportes/lista_reportes.html', context_instance = RequestContext(request))

#reporte entrada
def reporte_view_entrada(request): 
	if request.method == 'POST':
		formulario = busqueda_form(request.POST)
		if formulario.is_valid():
			fecha_inicio = formulario.cleaned_data['fecha_inicio']
			fecha_fin = formulario.cleaned_data['fecha_fin']
			lista_reporte = Entrada.objects.filter(fecha_ingreso__range=(fecha_inicio, fecha_fin))		
			ctx = {'repor': lista_reporte,'form': formulario}
			return render_to_response('reportes/reporte.html',ctx, context_instance = RequestContext(request))
	else:
		formulario = busqueda_form()
	ctx = {'form': formulario}
	return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))

#reporte salida
def reporte_view_salida(request):
	if request.method == "POST":
		formulario = busqueda_form(request.POST)
		if formulario.is_valid():
			fecha_inicio = formulario.cleaned_data['fecha_inicio']
			fecha_fin = forms.cleaned_data['fecha_fin']
			lista_reporte = Salida.objects.filter(fecha_salida__range=[fecha_inicio, fecha_fin])
			ctx = {'reporte' : lista_reporte,'form': formulario, 'opc' : opci}
			return render_to_response('reportes/reportes.html',ctx, context_instance = RequestContext(request))	
	else:
		formulario = busqueda_form()
	ctx = {'form': formulario}
	return render_to_response('reportes/reportes.html',ctx , context_instance=RequestContext(request))