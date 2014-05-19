from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'apps.news.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pets/', include('apps.animals.urls')),
    url(r'^news/', include('apps.news.urls')),
    url(r'^$', 'entry_list', {'template_name': 'homepage.html'}, name='homepage'),
)

urlpatterns = patterns(
    'django.contrib.flatpages.views',
    url(r'^/about/$', 'flatpage', {'url': '/about-us/'}, name='about'),
) + urlpatterns
