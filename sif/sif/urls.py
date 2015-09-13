from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
<<<<<<< HEAD


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sif.views.home', name='home'),
    url(r'^inventario/', include('sif.apps.inventario.urls')),
=======
import settings 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sif.views.home', name='home'),
    # url(r'^sif/', include('sif.foo.urls')),
>>>>>>> master

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('sif.apps.home.urls')),
<<<<<<< HEAD
    #url(r'^',include('sif.apps.inventario.urls')),

=======
    url(r'^',include('sif.apps.inventario.urls')),
    url(r'^',include('sif.apps.reportes.urls')),
    url(r'^',include('sif.apps.web_services.ws_producto.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
>>>>>>> master
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
