from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.add_post, name='add_post'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/notes/', views.notes, name='notes'),
    path('<int:post_id>/reblog/', views.reblog, name='reblog'),
    path('<int:post_id>/like/', views.like, name='like'),
]
