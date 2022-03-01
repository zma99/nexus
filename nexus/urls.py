from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
#from django.contrib.auth.views import login, logout_then_login
from .views import index, productos, resultado_busqueda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('resultado/', resultado_busqueda, name="resultado_busqueda"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
