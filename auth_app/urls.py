from django.conf.urls import url

from .views import LoginView


urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$',  LoginView.as_view()),
]
