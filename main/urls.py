from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect # Added this for the redirect

# Simple function to handle the empty home page
def home_redirect(request):
    return redirect('/admin/') # Redirects users to the admin login automatically

urlpatterns = [
    path("", home_redirect, name="home"), # This fixes the 404 error
    path("admin/", admin.site.urls),
    path("auth/", include("apis.urls")),
]

if settings.DEBUG:
    # These allow your images and CSS to load locally
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
