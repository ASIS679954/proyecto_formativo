from django.conf.urls.defaults import patterns, url
from django.conf.urls import include
from rest_framework import routers 
from sif.apps.web_services.ws_producto.views import *
router = routers.DefaultRouter()
router.register(r'productos', producto_viewset)
router.register(r'salida_producto', salida_producto_viewset)
router.register(r'codigo_barras',codigo_viewset)
router.register(r'sede',sede_viewset)
router.register(r'user',user_viewset)


urlpatterns = patterns('sif.apps.web_services.ws_producto.views',
		#url(r'^ws/producto/$','ws_productos_view', name = 'ws_productos_url'),
		url(r'^api/', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
	)