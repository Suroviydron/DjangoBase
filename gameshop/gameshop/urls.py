
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", include('adminapp.urls', namespace='admin')),
    path("", mainapp.main, name="main"),
    path('playstation/', include('mainapp.urls', namespace='playstation')),
    path("contact/", mainapp.contact, name="contact"),
    path('auth/', include('authnapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path("admin/", admin.site.urls)

