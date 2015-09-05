from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import add_product_form
from sif.apps.inventario.models import Producto
from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request) )

def  single_product_view(request, id_prod):
	prod = Producto.objects.get(id = id_prod)
	ctx = {'producto':prod}
	return render_to_response('home/single_producto.html',ctx,context_instance = RequestContext(request))
		
def productos_view(request):
	lista_prod = Producto.objects.all()
	ctx = {'Producto': lista_prod}
	return render_to_response('home/productos.html', ctx,context_instance = RequestContext(request))

def alerta_view(request, id_prod):
	clave = id_prod
	ctx = {'clave': clave }
	return render_to_response('home/alertaDelProducto.html',ctx, context_instance = RequestContext(request) )