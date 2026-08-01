from django.urls import path
from . import views

# These are the URL patterns for our playlists app.
# We map each URL pattern to a view function in views.py.
urlpatterns = [
    # The home route (e.g. http://127.0.0.1:8000/)
    path('', views.home, name='home'),
    
    # The playlist list page (e.g. http://127.0.0.1:8000/playlists/)
    path('playlists/', views.playlist_list, name='playlist_list'),
    
    # The playlist detail page (e.g. http://127.0.0.1:8000/playlists/1/)
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    
    # Simple JSON API route (e.g. http://127.0.0.1:8000/api/playlists/)
    path('api/playlists/', views.playlist_api_list, name='playlist_api_list'),
]
