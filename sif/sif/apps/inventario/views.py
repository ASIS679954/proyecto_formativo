from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.inventario.models import CodigoBarras
from sif.apps.inventario.models import Producto
from django.http import HttpResponseRedirect
import barcode
import time
import datetime




#Sedes
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
			edit_sede.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/sede/%s'% edit_sede.id)
	else: 
		formulario = add_sede_form(instance = sede)
	ctx = {'form':  formulario, 'informacion': info}
	return  render_to_response('inventario/edit_sede.html', ctx, context_instance = RequestContext(request))

#Entradas
def add_entrada_view(request):
	if request.method == "POST":
		formulario = add_entrada_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.cleaned_data['producto']
			cant = formulario.cleaned_data['cantidad']
			add = formulario.save(commit = False)
			if (cant > 0):
				prod.cantidad = prod.cantidad + cant
				prod.save()
				add.save()
				return HttpResponseRedirect('/entrada/%s' %add.id)
			else:
				formulario = add_entrada_form(instance = add)
				mensaje = "Error la cantidad debe ser mayor que 0"
				ctx = {'men':mensaje, 'form': formulario}
				return render_to_response('inventario/add_entrada.html', ctx, context_instance = RequestContext(request))
	else:
		formulario = add_entrada_form()
	ctx = {'form': formulario}
	return render_to_response('inventario/add_entrada.html', ctx, context_instance = RequestContext(request))

def edit_entrada_view(request, id_entr):
	entrada = Entrada.objects.get(pk =id_entr)
	cant_ini = entrada.cantidad
	prod = entrada.producto
	if request.method == "POST":
		formulario = add_entrada_form(request.POST, request.FILES,  instance= entrada)
		if formulario.is_valid():			
			cant_fin = formulario.cleaned_data['cantidad']
			edit_entrada = formulario.save(commit = False)
			if cant_fin > 0 :
				prod_aux = formulario.cleaned_data['producto']
				if prod.id == prod_aux.id:
					if cant_ini > cant_fin:
						cant_tol = cant_ini - cant_fin
						prod.cantidad = prod.cantidad - cant_tol
						prod.save()				
						edit_entrada.save()
						info = "Guardado satisfactoriamente"
						return HttpResponseRedirect('/entrada/%s'% edit_entrada.id)	
					else:
						cant_tol = cant_fin - cant_ini
						prod.cantidad = prod.cantidad + cant_tol
						prod.save()					
						edit_entrada.save()
						info = "Guardado satisfactoriamente"
						return HttpResponseRedirect('/entrada/%s'% edit_entrada.id)					
				else:
					prod.cantidad = prod.cantidad - cant_ini
					prod_aux.cantidad = prod_aux.cantidad + cant_fin
					prod.save()
					prod_aux.save()
					edit_entrada.save()				
					return HttpResponseRedirect('/entrada/%s'% edit_entrada.id)
			else:
				formulario = add_entrada_form(instance = entrada)
				mensaje = "Error, la cantidad debe ser mayor que o igual que 0"
				ctx = {'form':  formulario, 'men':mensaje}
				return  render_to_response('inventario/edit_entrada.html', ctx, context_instance = RequestContext(request))
	else: 
		formulario = add_entrada_form(instance = entrada)
	ctx = {'form':  formulario}
	return  render_to_response('inventario/edit_entrada.html', ctx, context_instance = RequestContext(request))

#Operador
def add_operador_view(request):
	info = "inicializando"
	if request.method =="POST":
		formulario = add_operador_form(request.POST,request.FILES)
		if formulario.is_valid():
			add =formulario.save(commit = False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect ('/operador/%s' %add.id)

	else:
		formulario = add_operador_form()
	ctx = {'form':formulario,'informacion':info}
	return render_to_response('inventario/add_operador.html',ctx,context_instance = RequestContext(request))


def edit_operador_view(request,id_operador):
	info=""
	ope = Usuario.objects.get(pk = id_operador)
	if request.method == "POST":
		formulario = add_operador_form(request.POST,request.FILES,instance = ope)
		if formulario.is_valid():
			edit_ope = formulario.save(commit = False)
			edit_ope.save
			info = "Guardado satisfactoriamente"
		return HttpResponseRedirect('/operador/%s'% edit_ope.id)
	else:
		formulario = add_operador_form(instance = ope)
	ctx = {'form':formulario,'informacion':info}
	return render_to_response('inventario/edit_operador.html',ctx,context_instance = RequestContext(request)) 


def inhabilitar_operador_view(request,id_operador):
	ope = Usuario.objects.get(pk = id_operador)
	ope.estado = False
	ope.save()
	info = "inhabilitado "
	return render_to_response('home/operador.html', context_instance = RequestContext(request)) #operarios es el nombre de mi url	

#Salida
def add_salida_view(request):
			
	if request.method == 'POST':
		formulario = add_salida_form(request.POST)
		if formulario.is_valid():
			prod = formulario.cleaned_data['producto']
			cant = formulario.cleaned_data['cantidad']
			aux =  prod.cantidad - cant
			add = formulario.save(commit = False)
			if (aux >= 0):
				prod.cantidad = aux
				prod.save()
				add.save()
				return HttpResponseRedirect('/salida/%s' %add.id)
			else:
				formulario = add_salida_form(instance = add)
				mensaje = "No se puede agregar esta salida la cantidad no esta disponible"
				ctx = {'men':mensaje, 'form': formulario}
				return render_to_response('inventario/add_salida.html', ctx, context_instance = RequestContext(request))
	else:
		formulario = add_salida_form()
	ctx = {'form': formulario}
	return render_to_response('inventario/add_salida.html', ctx , context_instance = RequestContext(request))

def edit_salida_view(request, id_sal):
	sali = Salida.objects.get(id = id_sal)
	cant_ini = sali.cantidad
	prod = sali.producto
	if request.method == 'POST':
		formulario = add_salida_form(request.POST, request.FILES, instance = sali)
		if formulario.is_valid():
			cant_fin = formulario.cleaned_data['cantidad']			
			edit_sal = formulario.save(commit = False)
			if cant_fin > 0:
				prod_aux = formulario.cleaned_data['producto']
				if prod.id == prod_aux.id:
					if cant_ini > cant_fin:
						cant_tol = cant_ini - cant_fin
						prod.cantidad = prod.cantidad + cant_tol
						prod.save()				
						edit_sal.save()
						info = "Guardado satisfactoriamente"
						return HttpResponseRedirect('/salida/%s'% edit_sal.id)	
					else:
						cant_tol = cant_fin - cant_ini
						prod.cantidad = prod.cantidad - cant_tol
						if prod.cantidad >= 0:
							prod.save()					
							edit_sal.save()
							info = "Guardado satisfactoriamente"
							return HttpResponseRedirect('/salida/%s'% edit_sal.id)
						else:
							formulario = add_salida_form(instance = edit_sal)
							mensaje = "No se puede agregar esta salida la cantidad no esta disponible"
							ctx = {'men':mensaje, 'form': formulario}
							return render_to_response('inventario/add_salida.html', ctx, context_instance = RequestContext(request))
				else:
					prod.cantidad = prod.cantidad + cant_ini
					prod_aux.cantidad = prod_aux.cantidad - cant_fin
					if prod_aux.cantidad >= 0:
						prod.save()
						prod_aux.save()
						edit_sal.save()				
						return HttpResponseRedirect('/salida/%s'% edit_sal.id)
					else:
						formulario = add_salida_form(instance = edit_sal)
						mensaje = "No se puede agregar esta salida la cantidad no esta disponible"
						ctx = {'men':mensaje, 'form': formulario}
						return render_to_response('inventario/edit_salida.html', ctx, context_instance = RequestContext(request))	
			else:
				formulario = add_salida_form(instance = sali)
				mensaje = "Error, la cantidad debe ser mayor que o igual que 0"
				ctx = {'form':  formulario, 'men':mensaje}
				return  render_to_response('inventario/edit_salida.html', ctx, context_instance = RequestContext(request))
			
	else:
		formulario = add_salida_form(instance = sali)
	ctx = {'form': formulario}
	return render_to_response('inventario/edit_salida.html', ctx , context_instance = RequestContext(request))

#Proveedor

def add_prove_view(request):
	info = "iniciando"
	if request.method=="POST":
		formulario = add_prove_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect ('/proveedores/')
	else:
		formulario = add_prove_form()
	ctx = {'form':formulario,'informacion': info}
	return render_to_response('inventario/add_proveedor.html',ctx, context_instance = RequestContext(request))


def edit_prove_view(request, id_prov):
	info = ""
	proveedor = Proveedor.objects.get(pk =id_prov)
	if request.method == "POST":
		formulario = add_prove_form(request.POST, request.FILES,  instance= proveedor)
		if formulario.is_valid():
			edit_prov = formulario.save(commit = False)
			edit_prov.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/proveedores/')
	else: 
		formulario = add_prove_form(instance = proveedor)
	ctx = {'form':  formulario, 'informacion': info}
	return  render_to_response('inventario/edit_proveedor.html', ctx, context_instance = RequestContext(request))


def creaCodigoAux():
	EAN = barcode.get_barcode_class('ean13')
	#En esta linea creo un ID0 basado en el tiempo de Unix a prueba de Hash Collision
	stamp = str((int(time.time())*100)+(datetime.datetime.now().second+10))
	ean = EAN(stamp)
	ean.save("sif/media/codes/"+stamp)
	crea = CodigoBarras(codigo=stamp)
	crea.save()
	cofre = CodigoBarras.objects.get(id=crea.id)
	return cofre


#Producto

def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.codigobarras = creaCodigoAux()
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s' %add.id)
	else:
		formulario = add_product_form()
	ctx = {'form':formulario,'informacion':info}
	return render_to_response('inventario/add_product.html', ctx,context_instance = RequestContext(request))

def edit_product_view(request, id_prod):
	info = ""
	prod = Producto.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES, instance= prod)
		if  formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			edit_prod.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s'% edit_prod.id)
	else:
		formulario = add_product_form(instance = prod)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response ('inventario/edit_product.html', ctx,context_instance = RequestContext(request))

def del_product_view(request, id_prod):
	
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect('/producto/')
	except:
		info = "Producto no se puede eliminar"	
		return HttpResponseRedirect('/producto/')



'''
 La vista creaCodigo: Crea un codigo sin necesidad de formulario, solo le hace falta 
 hacer un request post y automaticamente genera un codigo con ID unico y redirige a otro template
 donde se ve el codigo y la imagen del codigo generado 
'''
def creaCodigo(request):
	
	informacion = "Inicia"
	if request.method == "POST":
		informacion = "pasa post"
		EAN = barcode.get_barcode_class('ean13')
		#En esta linea creo un ID0 basado en el tiempo de Unix a prueba de Hash Collision
		stamp = str((int(time.time())*100)+(datetime.datetime.now().second+10))
		ean = EAN(stamp)
		ean.save("sif/media/codes/"+stamp)
		crea = CodigoBarras(codigo=stamp)
		crea.save()
		informacion = "Terminado"
        
		return HttpResponseRedirect('/codigoBarras/%s' %crea.id)
	else:
		formulario = "<input type='submit' name='envia' value='envia'>"
		
	ctx = {'form': formulario,'info':informacion}
	return render_to_response('inventario/agregaCB.html',ctx,context_instance = RequestContext(request))


'''
  La vista ver_unico: Muestra un codigo de barras y su imagen en base a su id 
'''
def ver_unico(request,id_cofre):
	cofre = CodigoBarras.objects.get(id=id_cofre)
	ctx = {'cofre':cofre}
	return render_to_response('inventario/muestraProducto.html',ctx,context_instance = RequestContext(request))
'''
  La vista ver_unico_cod: Muestra un codigo de barras y su imagen en base a su codigo 
'''
def ver_unico_cod(request,id_cofre):
	cofre = CodigoBarras.objects.get(codigo=id_cofre)
	ctx = {'cofre':cofre}
	return render_to_response('inventario/muestraProducto.html',ctx,context_instance = RequestContext(request))

        

