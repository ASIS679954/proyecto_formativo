from django.conf.urls.defaults import patterns, url 
#import settings

urlpatterns = patterns('sif.apps.inventario.views', 
		url(r'^add/producto/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/producto/(?P<id_prod>.*)/$', 'edit_product_view', name = 'vista_editar_productos' ),
		url(r'^del/producto/(?P<id_prod>.*)/$','del_product_view',name = 'vista_eliminar_producto'),


	)