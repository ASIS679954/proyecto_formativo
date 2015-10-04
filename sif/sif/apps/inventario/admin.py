from django.contrib import admin
from sif.apps.inventario.models import *
from sif.apps.home.models import *

admin.site.register(Usuario)
admin.site.register(Salida)
admin.site.register(Proveedor)
admin.site.register(Sede)
admin.site.register(Entrada)
admin.site.register(Producto)
admin.site.register(CodigoBarras)
admin.site.register(Referencia)