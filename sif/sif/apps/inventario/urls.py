from django.conf.urls import *


urlpatterns = patterns('sif.apps.inventario.views',
    url(r'^agregar/codigoBarras/$','creaCodigo',name = 'vista_agregar_codigo'),
           
           
)