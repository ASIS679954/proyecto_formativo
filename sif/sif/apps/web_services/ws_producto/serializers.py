from rest_framework import serializers
from sif.apps.inventario.models import *


class producto_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('url','nombre', 'cantidad','valor')

class salida_producto_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Salida
		fields = ('url','fecha_salida','codigobarras', 'sede','tipo_salida', 'cantidad', 'descripcion', 'numero_contrato')


class codigo_barras_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CodigoBarras
		fields = ('url','codigo')

class sede_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sede
		fields = ('url','nombre_sede')



