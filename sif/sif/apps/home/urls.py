from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('sif.apps.home.views',

	url(r'^sede/(?P<id_sede>.*)/$', 'single_sede_view', name = 'vista_single_sede'),
	url(r'^sedes/$', 'sede_view' , name = 'vista_sede'),
		
	) 

