from django.http import HttpResponse
from sif.apps.inventario.models import *
from django.core import serializers
from .serializers import *
from rest_framework import viewsets

class producto_viewset(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = producto_serializer

class salida_producto_viewset(viewsets.ModelViewSet):
	queryset = Salida.objects.all()
	serializer_class = salida_producto_serializer

class codigo_viewset(viewsets.ModelViewSet):
	queryset = CodigoBarras.objects.all()
	serializer_class = codigo_barras_serializer

class sede_viewset(viewsets.ModelViewSet):
	queryset = Sede.objects.all()
	serializer_class = sede_serializer

class user_viewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = user_serializer
