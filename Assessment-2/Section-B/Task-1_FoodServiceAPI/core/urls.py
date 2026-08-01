from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the api urls under the /api/ path
    path('api/', include('api.urls')),
]
