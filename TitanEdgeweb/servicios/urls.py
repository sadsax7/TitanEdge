#url valido unicamente para esta app
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#directorio propio
urlpatterns = [
    path('', views.servicios, name="Servicios"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)