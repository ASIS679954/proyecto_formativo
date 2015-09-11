from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import add_product_form
from sif.apps.inventario.models import Producto
from django.http import HttpResponseRedirect


def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
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

	if user.is_autheticated and user.is_staff:
		info = "inicializando"
		try:
			prod = Producto.objects.get(pk = id_prod)
			prod.delete()
			info = "Producto Eliminado Correctamente"
			return HttpResponseRedirect('/producto/')
		except:
			info = "Producto no se puede eliminar"	
			return HttpResponseRedirect('/producto/')
	else: 
		return HttpResponseRedirect('/producto/')
	
	