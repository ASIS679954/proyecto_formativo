from django.contrib import admin
from sif.apps.inventario.models import *

admin.site.register(Usuario)
#admin.site.register(Municipio)

#admin.site.register(Transferencia)
admin.site.register(Salida)
admin.site.register(Rol)
admin.site.register(Proveedor)
admin.site.register(Sede)
admin.site.register(Entrada)
admin.site.register(Departamento)
admin.site.register(Producto)


admin.site.register(CodigoBarras)