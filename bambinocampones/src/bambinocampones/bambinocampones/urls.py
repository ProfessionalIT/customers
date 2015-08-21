from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'', include('website.urls')),
                       ) + static(settings.MEDIA_URL,
                                  document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'media/(?P<path>.*)',
                             'serve', {'document_root': settings.MEDIA_ROOT}),)
