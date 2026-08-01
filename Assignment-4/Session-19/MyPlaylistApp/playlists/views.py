from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse  # Added to return JSON data for the API
from .models import Playlist

# The view function for the Home Page
def home(request):
    # This renders the home.html template from our templates directory
    return render(request, 'playlists/home.html')

# The view function to display all Playlists
def playlist_list(request):
    # Retrieve all playlists stored in our SQLite database
    all_playlists = Playlist.objects.all().order_by('-created_at')
    
    # We pass the playlists inside a context dictionary to the template
    context = {
        'playlists': all_playlists
    }
    return render(request, 'playlists/playlist_list.html', context)

# The view function to display a single Playlist details
def playlist_detail(request, playlist_id):
    # This gets the playlist matching the ID, or returns a 404 page if it doesn't exist
    single_playlist = get_object_or_404(Playlist, id=playlist_id)
    
    # Pass the single playlist to the detail page template
    context = {
        'playlist': single_playlist
    }
    return render(request, 'playlists/playlist_detail.html', context)

# A simple JSON API endpoint that returns all playlists
# This is useful if students need to demonstrate building an API
def playlist_api_list(request):
    playlists = Playlist.objects.all().order_by('-created_at')
    
    # Manually build a list of dictionaries to serialize into JSON
    playlist_data = []
    for item in playlists:
        # Fetch songs for this playlist
        songs_list = []
        for song in item.songs.all():
            songs_list.append({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'audio_url': song.audio_file.url if song.audio_file else None,
                'song_image': song.song_image.url if song.song_image else None,
            })

        playlist_data.append({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            # If there's an image, return its URL, otherwise None
            'cover_image': item.cover_image.url if item.cover_image else None,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'songs': songs_list  # Include the list of songs
        })
        
    # Return the data as JSON. safe=False is needed because we are returning a list, not a dict.
    return JsonResponse(playlist_data, safe=False)
