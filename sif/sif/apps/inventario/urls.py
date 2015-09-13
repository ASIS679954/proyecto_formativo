from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.inventario.views',
		#Sede
		url(r'^add/sede/$','add_sede_view', name = 'vista_agregar_sede'),
		url(r'^edit/sede/(?P<id_sede>.*)/$', 'edit_sede_view', name = 'vista_editar_sede'),
		#Entrada
		url(r'^add/entrada/$','add_entrada_view', name = 'vista_agregar_entrada'),
		url(r'^edit/entrada/(?P<id_entr>.*)/$', 'edit_entrada_view', name = 'vista_editar_entrada'),
		#Operador
		url(r'^add/operador/$','add_operador_view',name = 'vista_agregar_operador'),
		url(r'^edit/operador/(?P<id_operador>.*)/$','edit_operador_view', name = 'vista_editar_operador'),
		url(r'^inh/operador/(?P<id_operador>.*)/$','inhabilitar_operador_view',name = 'vista_inhabilitar_operador'),
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

		url(r'^agregar/codigoBarras/$','creaCodigo',name = 'vista_agregar_codigo'),
		url(r'^codigoBarras/(?P<id_cofre>.*)/$','ver_unico',name = 'vista_ver_unico'),

	)



