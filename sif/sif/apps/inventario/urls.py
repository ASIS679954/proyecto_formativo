from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.inventario.views',

		#codigo_barras
    	url(r'^agregar/codigoBarras/$','creaCodigo',name = 'vista_agregar_codigo'),
		url(r'^codigoBarras/(?P<id_cofre>.*)/$','ver_unico',name = 'vista_ver_unico'),
	
 		#Sede
		url(r'^add/sede/$','add_sede_view', name = 'vista_agregar_sede'),
		url(r'^edit/sede/(?P<id_sede>.*)/$', 'edit_sede_view', name = 'vista_editar_sede'),
		#Entrada
		url(r'^add/entrada/$','add_entrada_view', name = 'vista_agregar_entrada'),
		url(r'^edit/entrada/(?P<id_entr>.*)/$', 'edit_entrada_view', name = 'vista_editar_entrada'),
		#Salida
		url(r'^add/salida/$','add_salida_view', name = 'vista_agregar_salida'), 
		url(r'^edit/salida/(?P<id_sal>.*)/$','edit_salida_view', name = 'vista_editar_salida'), 
		#Proveedor
		url(r'^add/proveedor/$','add_prove_view', name = 'vista_agregar_proveedor'), 
		url(r'^edit/proveedor/(?P<id_prov>.*)/$','edit_prove_view', name = 'vista_editar_proveedor'), 
		#Producto
		url(r'^add/producto/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/producto/(?P<id_prod>.*)/$', 'edit_product_view', name = 'vista_editar_productos' ),
		url(r'^del/producto/(?P<id_prod>.*)/$','del_product_view',name = 'vista_eliminar_producto'),
		#codigo Barras
		url(r'^agregar/codigoBarras/$','creaCodigo',name = 'vista_agregar_codigo'),
		url(r'^codigoBarras/cod/(?P<id_cofre>.*)/$','ver_unico_cod',name = 'vista_ver_unico_cod'),
		url(r'^codigoBarras/(?P<id_cofre>.*)/$','ver_unico',name = 'vista_ver_unico'),



	)

