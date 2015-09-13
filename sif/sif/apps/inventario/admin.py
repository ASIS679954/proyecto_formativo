from django.contrib import admin
from sif.apps.inventario.models import *

admin.site.register(Usuario)
#admin.site.register(Municipio)

#admin.site.register(Transferencia)
admin.site.register(Salida)
admin.site.register(Rol)
admin.site.register(Proveedor)
admin.site.register(Sede)
<<<<<<< HEAD
admin.site.register(Entrada)
admin.site.register(Departamento)
admin.site.register(Producto)

=======
#admin.site.register(Municipio)
admin.site.register(Departamento)
admin.site.register(Producto)
#admin.site.register(Transferencia)
>>>>>>> 46010739e8407bdf4c7b1e657a4b580cf52010d7
admin.site.register(CodigoBarras)