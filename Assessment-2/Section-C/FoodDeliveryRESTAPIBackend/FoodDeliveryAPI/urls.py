from django.contrib import admin
from django.urls import path, include
from foodapp.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('foodapp.urls')),
]
