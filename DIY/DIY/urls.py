from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

#if settings.DEBUG:         #if DEBUG== True, static will arrive form this directory
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
