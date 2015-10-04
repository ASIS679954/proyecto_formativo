from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.home.views',
	
	#index
	url(r'^$', 'index_view' , name = 'vista_index'),
	#Sede
	url(r'^sede/(?P<id_sede>.*)/$', 'single_sede_view', name = 'vista_single_sede'),
	url(r'^sedes/$', 'sede_view' , name = 'vista_sede'),
	#Entrada
	url(r'^entrada/(?P<id_entr>.*)/$', 'single_entrada_view', name = 'vista_single_entrada'),
	url(r'^entradas/$', 'entrada_view' , name = 'vista_entrada'),
	#Usuario
	url(r'^usuario/(?P<id_user>.*)/$','single_usuario_view',name = 'vista_ver_usuario'),
	url(r'^edit/user/(?P<id_user>.*)/$','edit_user_view',name = 'vista_editar_usuario'),
	url(r'^edit/pass/(?P<id_user>.*)/$','edit_pass_view',name = 'vista_editar_usuario_pass'),
	url(r'^usuarios_adm/$','usuarios_admin_activos_view',name = 'vista_usuarios_admin'),	
	url(r'^usuarios_opr/$','usuarios_oper_activos_view',name = 'vista_usuarios_oper'),	
	url(r'^usuarios_inac_adm/$','usuarios_admin_inactivos_view',name = 'vista_usuarios_inac_admin'),	
	url(r'^usuarios_inac_opr/$','usuarios_oper_inactivos_view',name = 'vista_usuarios_inac_oper'),	
	url(r'^list_usuarios/$','list_usuarios_view',name = 'vista_lista_usuarios'),	
	url(r'^inh_user/(?P<id_user>.*)$','inhabilitar_user_view',name = 'vista_inhabilitar_usuario'),	
	url(r'^act_user/(?P<id_user>.*)$','habilitar_user_view',name = 'vista_habilitar_usuario'),	
	#Salida
	url(r'^salida/(?P<id_sal>.*)/$','single_salida_view', name = 'vista_single_salida'), 
	url(r'^salidas/$','salidas_view', name = 'vista_salida'), 
	#Proveedor
	url(r'^proveedores/$','proveedor_view', name = 'vista_proveedor'), 
	#Producto
	url(r'^alerta/(?P<id_prod>.*)/$', 'alerta_view', name = 'vista_alerta'), 
	url(r'^producto/(?P<id_prod>.*)/$', 'single_product_view' , name = 'vista_single_producto'),
	url(r'^producto/$', 'productos_view', name = 'vista_productos'),	
	#Registro usuario
	url(r'^registro/$','register_view', name = 'vista_registro'),
	#login - logout
	url(r'^login/$', 'login_view', name = "vista_login"),
	url(r'^logout/$', 'logout_view', name = "vista_logout"),
	
	#Cootizacion
	url(r'^cotizacion/$', 'cotizacion_view' , name = 'vista_cotizacion'),	

)

