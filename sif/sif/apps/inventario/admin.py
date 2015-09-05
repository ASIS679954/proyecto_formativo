from django.contrib import admin
from sif.apps.inventario.models import *

admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(Sede)
admin.site.register(Departamento)
admin.site.register(Producto)
admin.site.register(Salida)
admin.site.register(CodigoBarras)
admin.site.register(Rol)