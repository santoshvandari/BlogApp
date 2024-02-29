from django.contrib import admin
from django.urls import path,include
from froala_editor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('froala_editor/',include('froala_editor.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
