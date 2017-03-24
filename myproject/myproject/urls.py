
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^myproject/$', 'myproyect.views.dame_pelis'),
    url(r'^myproject/(\d+)', 'myproject.views.pelicula'),
    url(r'^myproject/(.+)/(.+)/(.*)', 'myproject.views.nuevapeli'),
    url(r'^admin/', include(admin.site.urls)),
]
