from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: HttpResponse("Backend Running Successfully 🚀")),
    path("admin/", admin.site.urls),
    path("auth/", include("tables.urls")),
]
