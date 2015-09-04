# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FormuCrea

def creaCodigo(request):

	if request.method == 'POST': 
		form = FormuCrea(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/agregado/')
	else:
		form = FormuCrea()
	return render(request, 'formulario.html',{'form': form})
