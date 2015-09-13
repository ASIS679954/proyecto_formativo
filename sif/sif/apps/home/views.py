# Create your views here.
<<<<<<< HEAD
=======
from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.inventario.models import *
from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))

#Sede
def single_sede_view(request,id_sede):
	sede = Sede.objects.get(id = id_sede)
	ctx = {'sede': sede}
	return render_to_response('home/single_sede.html', ctx, context_instance = RequestContext(request))

def sede_view(request):
	lista_sede = Sede.objects.all()
	ctx = {'sede': lista_sede}
	return render_to_response ('home/sedes.html', ctx, context_instance = RequestContext(request))

#Entrada
def single_entrada_view(request,id_entr):
	entrada = Entrada.objects.get(id = id_entr)
	ctx = {'entra': entrada}
	return render_to_response('home/single_entrada.html', ctx, context_instance = RequestContext(request))

def entrada_view(request):
	lista_entrada = Entrada.objects.all()
	ctx = {'entra': lista_entrada}
	return render_to_response ('home/entrada.html', ctx, context_instance = RequestContext(request))

#Operador
def single_operador_view(request,id_oper):
	oper = Usuario.objects.get(id =id_oper)
	ctx = {'opera':oper}
	return render_to_response('home/single_operador.html',ctx,context_instance= RequestContext(request))
	

def operarios_view(request):
	lista_operarios = Usuario.objects.filter(estado = True)
	ctx = {'opera':lista_operarios}
	return render_to_response('home/operador.html',ctx,context_instance =RequestContext(request))

#Salida

def single_salida_view(request, id_sal):
	sali = Salida.objects.get(pk = id_sal)
	ctx = {'salida': sali}
	return render_to_response('home/single_salida.html', ctx,  context_instance =RequestContext(request))

def salidas_view(request):
	sali = Salida.objects.all()
	ctx = {'salida': sali}
	return render_to_response('home/salidas.html', ctx, context_instance = RequestContext(request))

#Proveedor

def proveedor_view(request):
	prov = Proveedor.objects.all()
	ctx = {'proveedores': prov}
	return render_to_response('home/proveedor.html', ctx, context_instance = RequestContext(request))

#Producto
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
>>>>>>> master
