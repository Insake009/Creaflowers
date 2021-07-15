from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('contacts/', include('contacts.urls')),
        path('flowers/', include('flowers.urls')),
        path('orders/', include('orders.urls'))
    ])),
] + docs

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
