from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'apps.news.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w\-]+)/$', 'entry_detail', name='entry_detail'),
    url(r'^$', 'entry_list', name='entry_list'),
)
