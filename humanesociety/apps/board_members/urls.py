from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'apps.board_members.views',
    url(r'^$', 'board_list', name='board_list'),
)
