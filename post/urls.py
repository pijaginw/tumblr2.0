from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<post_id>[0-9]+)/notes/$', views.notes, name='notes'),
    url(r'^(?P<post_id>[0-9]+)/reblog/$', views.reblog, name='reblog'),
    url(r'^(?P<post_id>[0-9]+)/like/$', views.like, name='like'),
]
