from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.inventario.views',
		url(r'^add/sede/$','add_sede_view', name = 'vista_agregar_sede'),
		url(r'^edit/sede/(?P<id_sede>.*)/$', 'edit_sede_view', name = 'vista_editar_sede'),

			)
	