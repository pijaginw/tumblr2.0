from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^dashboard/', include('dashboard.urls')),
#     url(r'^post/', include('post.urls')),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('post/', include('post.urls', namespace='post')),
]
