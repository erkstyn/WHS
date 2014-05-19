from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'apps.animals.views',
    url(r'^adopt/(?P<slug>[\w\-]+)/$', 'adoption_detail', name='adoption_detail'),
    url(r'^(?P<species>[\w\-]+)/$', 'adoption_list', name='adoption_list_species'),
    url(r'^(?P<species>[\w\-]+)/(?P<breed>[\w\-]+)/$', 'adoption_list', name='adoption_list_species_breed'),
    url(r'^$', 'adoption_list', name='adoption_list'),
)
