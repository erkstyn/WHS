from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
from django.conf import settings

def get_recent_candidates():
    from apps.animals.models import AdoptionCandidate

    return {
        'recently_added': AdoptionCandidate.objects.available()[0:3] 
    }

urlpatterns = patterns(
    'apps.news.views',
    url(r'^board/', include('apps.board_members.urls')),
    url(r'^pets/', include('apps.animals.urls')),
    url(r'^news/', include('apps.news.urls')),
    url(r'^$', 'entry_list', {
        'template_name': 'homepage.html',
        'get_context': get_recent_candidates,
    }, name='homepage'),
)

if settings.ADMIN_ENABLED:
    admin.autodiscover()
    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
    ) + urlpatterns

urlpatterns = patterns(
    'django.contrib.flatpages.views',
    url(r'^/about/$', 'flatpage', {'url': '/about-us/'}, name='about'),
) + urlpatterns
