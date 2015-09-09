from django.conf.urls import *


urlpatterns = patterns('sif.apps.inventario.views',
    url(r'^agregar/codigoBarras/$','creaCodigo',name = 'vista_agregar_codigo'),
	url(r'^codigoBarras/(?P<id_cofre>.*)/$','ver_unico',name = 'vista_ver_unico'),
	
           
           
)