"""
URL configuration for MyPlaylistApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # We added include here
from django.conf import settings  # To access base settings like MEDIA_URL
from django.conf.urls.static import static  # Helper function to serve static/media files in dev

urlpatterns = [
    # Django Admin site
    path('admin/', admin.site.urls),
    
    # We forward all other paths to the playlists app's urls.py
    path('', include('playlists.urls')),
]

# This allows Django to serve uploaded images (media files) and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
