from django.conf.urls.defaults import *


urlpatterns = patterns('sif.apps.inventario.views',
    url(r'^agregar/codigoBarras/$','creaCodigo',name = 'vista_agregar_codigo'),
           
           
)