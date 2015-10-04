from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.inventario.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from sif.apps.home.forms import *
from django.contrib.auth import login, logout , authenticate



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

#Usuario

def list_usuarios_view(request):
	return render_to_response('home/lista_usuarios.html', context_instance = RequestContext(request))


def single_usuario_view(request,id_user):
	user = Usuario.objects.get(id =id_user)
	ctx = {'user':user}
	return render_to_response('home/single_usuario.html',ctx,context_instance= RequestContext(request))
	
def usuarios_admin_activos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = True, user__is_active = True)
	ctx = {'users':lista_usuarios, 'title': 'Lista Administradores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def usuarios_admin_inactivos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = True, user__is_active = False)
	ctx = {'users':lista_usuarios, 'title': 'Lista Administradores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def usuarios_oper_activos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = False, user__is_active = True)
	ctx = {'users':lista_usuarios, 'title': 'Lista Operadores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def usuarios_oper_inactivos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = False, user__is_active = False)
	ctx = {'users':lista_usuarios, 'title': 'Lista Operadores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def inhabilitar_user_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	userito = userito.user
	userito.is_active = False
	userito.save()
	if userito.is_superuser == True:	
		return HttpResponseRedirect('/usuarios_adm/')
	else:
		return HttpResponseRedirect('/usuarios_opr/')

def habilitar_user_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	userito = userito.user
	userito.is_active = True
	userito.save()
	if userito.is_superuser == True:	
		return HttpResponseRedirect('/usuarios_inac_adm/')
	else:
		return HttpResponseRedirect('/usuarios_inac_opr/')

def edit_user_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	usua = userito.user
	iden = userito.id
	formulario = edit_user_form(instance = userito)
	if request.method == "POST":
		formulario = edit_user_form(request.POST, instance = userito)
		if formulario.is_valid():
			edit_user = formulario.save(commit = False)
			username = formulario.cleaned_data['identificacion']
			edit_user.save()
			usua.username = username
			tipo = formulario.cleaned_data['tipo']
			formulario.save()
			if tipo == "admin":
				usua.is_superuser = True
				usua.is_staff = False
			else:
				usua.is_staff = True
				usua.is_superuser = False
			usua.save()
			return HttpResponseRedirect('/list_usuarios')
	ctx = {'form': formulario, 'id': iden}
	return render_to_response('home/edit_user.html', ctx, context_instance = RequestContext(request))

def edit_pass_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	formulario = edit_pass_form()
	if request.method == "POST":
		formulario = edit_pass_form(request.POST)
		if formulario.is_valid():
			userito.user.set_password(formulario.cleaned_data['password_one'])
			userito.save()
			return HttpResponseRedirect('/list_usuarios')
	ctx = {'form': formulario}
	return render_to_response('home/edit_pass.html', ctx, context_instance = RequestContext(request))

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


#Registro de usuario
def register_view(request):
	form = RegisterForm()
	form_oper = add_usuario_form()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		form_oper = add_usuario_form(request.POST)
		if form.is_valid() and form_oper.is_valid():
			email 	= form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			tipo = form.cleaned_data['tipo']		
			username = form_oper.cleaned_data['identificacion']
			u = User.objects.create_user(username = username, email = email, password = password_one)
			u.save()
			if tipo == "admin":
				u.is_superuser  = True
			else:
				u.is_staff = True
			u.save()		
			add_usuario = form_oper.save(commit = False)
			add_usuario.user = u
			add_usuario.save()
			return HttpResponseRedirect('/usuarios_adm')
		else:
			ctx = {'form': form, 'form_oper': form_oper}
			return render_to_response('home/registro.html', ctx, context_instance = RequestContext(request))
	ctx = {'form': form, 'form_oper': form_oper}
	return render_to_response('home/registro.html', ctx, context_instance = RequestContext(request))


#Login - logout

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form': formulario, 'men': mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


#Generar cootizacion

def cotizacion_view(request):
	info_enviado = False 
	nombre		= ""
	apellido	= ""
	direccion	= ""
	telefono	= ""
	sede		= ""
	cantidad	= ""
	producto	= ""
	email		= ""
	observacion	= ""

	lista = []
	detalle =[]


	agregado = False

	if request.method == "POST":
		formulario = cotizacion_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			nombre		= formulario.cleaned_data['nombre']
			apellido	= formulario.cleaned_data['apellido']
			direccion	= formulario.cleaned_data['direccion']
			telefono	= formulario.cleaned_data['telefono']
			sede		= formulario.cleaned_data['sede']
			producto	= formulario.cleaned_data['producto']
			cantidad	= formulario.cleaned_data['cantidad']
			email 		= formulario.cleaned_data['email']
			observacion	= formulario.cleaned_data['observacion']
			
			i = producto.id

			detalle.append(producto.nombre)
			detalle.append(producto.cantidad)
			detalle.append(producto.valor)

			detalle.append(producto.valor * producto.cantidad)

			lista.append(detalle)
			detalle=[]

			print lista 
	else:	
		formulario = cotizacion_form()
	ctx = {'form': formulario,'nombre':nombre,'apellido':apellido,'direccion':direccion,'telefono':telefono,'sede':sede,'cantidad':cantidad,'producto':producto,'email':email,'observacion':observacion,"info_enviado":info_enviado}
	return render_to_response('home/cotizacion.html',ctx,context_instance = RequestContext(request))
