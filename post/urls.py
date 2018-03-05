from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'post'

# urlpatterns = [
#     url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<post_id>[0-9]+)/notes/$', views.notes, name='notes'),
#     url(r'^(?P<post_id>[0-9]+)/reblog/$', views.reblog, name='reblog'),
#     url(r'^(?P<post_id>[0-9]+)/like/$', views.like, name='like'),
# ]
urlpatterns = [
    path('', views.add_post, name='add_post'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/notes/', views.notes, name='notes'),
    path('<int:post_id>/reblog/', views.reblog, name='reblog'),
    path('<int:post_id>/like/', views.like, name='like'),
]
