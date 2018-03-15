from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('post/', include('post.urls', namespace='post')),
    path('user/', include('user.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
