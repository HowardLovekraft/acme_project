from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
]

if settings.DEBUG:
    # Set debug tools
    from  debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()

    # Render media via Django, not via Nginx-like tool
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)