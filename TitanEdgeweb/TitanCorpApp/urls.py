#url valido unicamente para esta app
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#directorio propio
urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)