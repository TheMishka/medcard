from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^searchresult/$', views.searchresult, name = 'searchresult'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^new_person/$', views.new_person, name = 'new_person'),
    url(r'^(?P<person_id>\d+)/$', views.personcard, name='personcard'),
    url(r'^(?P<person_id>\d+)/docedit/(?P<doc_id>\d+)$', views.doc_edit, name='docedit'),
    url(r'^(?P<person_id>\d+)/docedit/$', views.doc_edit, name='newdoc'),
    url(r'^[a-z0-9-]+/docdel/$', views.doc_del, name='docdel'),
    url(r'^(?P<person_id>\d+)/edit/$', views.card_edit, name='card_edit'),
    url(r'^(?P<person_id>\d+)/diagstree/(?P<relation_id>\d+)$', views.diags_edit, name='edit_diags'),
    url(r'^(?P<person_id>\d+)/diagstree/$', views.diags_edit, name='new_diags'),
    url(r'^[a-z0-9-]+/diagdel/$', views.diag_del, name='del_diags'),
]