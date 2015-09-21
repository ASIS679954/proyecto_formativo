# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.inventario.models import *
from django.http import HttpResponseRedirect

def single_sede_view(request,id_sede):
	sede = Sede.objects.get(id = id_sede)
	ctx = {'sede': sede}
	return render_to_response('home/single_sede.html', ctx, context_instance = RequestContext(request))

def sede_view(request):
	lista_sede = Sede.objects.all()
	ctx = {'sede': lista_sede}
	return render_to_response ('home/sedes.html', ctx, context_instance = RequestContext(request))

