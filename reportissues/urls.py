from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'', include('manageuser.urls')),
    url(r'', include('manageproject.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
        'show_indexes': True}),
    url(r'',
        include('django.contrib.staticfiles.urls')),
    
    
)+ staticfiles_urlpatterns()


