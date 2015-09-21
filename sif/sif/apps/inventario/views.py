# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from sif.apps.inventario.forms import FormuCrea
from sif.apps.inventario.models import CodigoBarras
from sif.apps.inventario.models import Producto
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
			ean.save(request.POST.get('codigo'))
 			agrega = formulario.save(commit = False)
			agrega.save()
			informacion = "Terminado"
			return HttpResponseRedirect('/codigoBarras/%s' %agrega.id)
	else:
		tablaCofre = CodigoBarras.objects().all()
		formulario = FormuCrea()
		ctx = {'form': formulario,'info':informacion,'tabla':tablaCofre}
	return render_to_response('inventario/agregaCB.html',ctx,context_instance = RequestContext(request))

def ver_unico(request,id_cofre):
	cofre = CodigoBarras.objects.get(id=id_cofre)
	pp = Producto.objects.select_related().get(id)
	ctx = {'cofre':cofre,'pp':pp}
	return render_to_response('inventario/muestraProducto.html',ctx,context_instance = RequestContext(request))



def add_sede_view(request):
	info = "iniciando"
	if request.method=="POST":
		formulario = add_sede_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect ('/sede/%s' %add.id)
	else:
		formulario = add_sede_form()
	ctx = {'form':formulario,'informacion': info}
	return render_to_response('inventario/add_sede.html',ctx, context_instance = RequestContext(request))


def edit_sede_view(request, id_sede):
	info = ""
	sede = Sede.objects.get(pk =id_sede)
	if request.method == "POST":
		formulario = add_sede_form(request.POST, request.FILES,  instance= sede)
		if formulario.is_valid():
			edit_sede = formulario.save(commit = False)
			formulario.save_m2m()
			edit_sede.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/sede/%s'% edit_sede.id)
	else: 
		formulario = add_sede_form(instance = sede)
	ctx = {'form':  formulario, 'informacion': info}
	return  render_to_response('inventario/edit_sede.html', ctx, context_instance = RequestContext(request))

