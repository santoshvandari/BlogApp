from django.contrib import admin
from django.urls import path,include
from froala_editor import views
from django.conf import settings
from django.conf.urls.static import static
from Home import views

urlpatterns = [
    path('login/', admin.site.urls),
    path('',include('Home.urls')),
    path('froala_editor/',include('froala_editor.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'Home.views.custom_404'

admin.site.site_title = "Blog Website Portal"
admin.site.site_header = "Blog Website"
admin.site.index_title = "Welcome to Blog Website Portal"
