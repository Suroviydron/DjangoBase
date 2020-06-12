from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path
from django.conf.urls.static import static

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^admin/", include('adminapp.urls', namespace='admin')),
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^playstation/", include('mainapp.urls', namespace='playstation')),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    re_path(r"^auth/", include('authnapp.urls', namespace='auth')),
    re_path(r"^basket/", include('basketapp.urls', namespace='basket')),
    path("", include("social_django.urls", namespace="social"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path("admin/", admin.site.urls)

