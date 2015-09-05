from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.home.views',
		url(r'^index/$', 'index_view', name = 'vista_index'), 
		url(r'^producto/(?P<id_prod>.*)/$', 'single_product_view' , name = 'vista_single_producto'),
		url(r'^producto/$', 'productos_view', name = 'vista_productos'),
	
	)	