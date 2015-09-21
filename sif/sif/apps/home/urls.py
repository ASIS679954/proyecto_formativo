from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.home.views',

<<<<<<< HEAD
	url(r'^sede/(?P<id_sede>.*)/$', 'single_sede_view', name = 'vista_single_sede'),
	url(r'^sedes/$', 'sede_view' , name = 'vista_sede'),
		
	) 

=======
	#index
	url(r'^$', 'index_view' , name = 'vista_index'),
	#Sede
	url(r'^sede/(?P<id_sede>.*)/$', 'single_sede_view', name = 'vista_single_sede'),
	url(r'^sedes/$', 'sede_view' , name = 'vista_sede'),
	#Entrada
	url(r'^entrada/(?P<id_entr>.*)/$', 'single_entrada_view', name = 'vista_single_entrada'),
	url(r'^entradas/$', 'entrada_view' , name = 'vista_entrada'),
	#Operador
	url(r'^operador/(?P<id_oper>.*)/$','single_operador_view',name = 'vista_ver_operador'),
	url(r'^operarios/$','operarios_view',name = 'vista_operarios'),	
	#Salida
	url(r'^salida/(?P<id_sal>.*)/$','single_salida_view', name = 'vista_single_salida'), 
	url(r'^salidas/$','salidas_view', name = 'vista_salida'), 
	#Proveedor
	url(r'^proveedores/$','proveedor_view', name = 'vista_proveedor'), 
	#Producto
	url(r'^alerta/(?P<id_prod>.*)/$', 'alerta_view', name = 'vista_alerta'), 
	url(r'^producto/(?P<id_prod>.*)/$', 'single_product_view' , name = 'vista_single_producto'),
	url(r'^producto/$', 'productos_view', name = 'vista_productos'),
	 

)
>>>>>>> origin/esteban
