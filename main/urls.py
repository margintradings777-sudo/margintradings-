from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # APIs (login, register, withdrawal, deposit etc)
    path("apis/v1/", include("apis.urls")),

    # Tables app (profile view etc)
    path("", include("tables.urls")),
]

# Media files (PAN image, bank document etc)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
