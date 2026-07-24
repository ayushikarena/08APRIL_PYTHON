# urls.py
# Main URL routing configuration for restaurant_project.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin site route
    path('admin/', admin.site.urls),
    
    # Include all URLs from our 'restaurants' application
    path('', include('restaurants.urls')),
]

# Serve media files in development environment
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
