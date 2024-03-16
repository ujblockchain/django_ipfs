from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    # admin path
    path(f'{settings.ADMIN_PATH}/', admin.site.urls),
    path('', include('djfsender.urls')),
]

# update urlpatterns if debug is true
if settings.DEBUG:
    urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
