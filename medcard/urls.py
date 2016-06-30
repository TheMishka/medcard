from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^searchresult/$', views.searchresult, name = 'searchresult'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^new_person/$', views.new_person, name = 'new_person'),
    url(r'^(?P<person_id>\d+)/$', views.personcard, name='personcard'),
    url(r'^(?P<person_id>\d+)/edit/$', views.card_edit, name = 'card_edit'),
)