from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('pages.urls')),
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
]

if settings.DEBUG:
    # Set debug tools (for Django 3)
    import debug_toolbar

    urlpatterns += (
        path('__debug__/', include(debug_toolbar.urls)),
    )

    # Render media via Django, not via Nginx-like tool
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


handler404 = 'core.views.page_not_found'
