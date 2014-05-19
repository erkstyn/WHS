from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'www.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'homepage', name='homepage'),
)

urlpatterns = patterns(
    'django.contrib.flatpages.views',
    url(r'^/about/$', 'flatpage', {'url': '/about-us/'}, name='about'),
) + urlpatterns
