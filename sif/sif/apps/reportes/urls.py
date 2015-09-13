from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('sif.apps.reportes.views',
	url(r'^busqueda/$','busqueda_view', name = 'vista_busqueda'),

)