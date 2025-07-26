from django.urls import include, path

from .views import MyUserCreateView


urlpatterns = [
    path('registration/', MyUserCreateView.as_view(), name='registration'),
    path('', include('django.contrib.auth.urls')),
]
