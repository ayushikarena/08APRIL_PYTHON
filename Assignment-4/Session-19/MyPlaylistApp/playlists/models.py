from django.db import models

# This is our model for Playlists. A model represents a table in the database.
class Playlist(models.Model):
    # The title of the playlist (e.g. "My Chill Mix")
    title = models.CharField(max_length=100)
    
    # A longer description of what this playlist is about
    description = models.TextField()
    
    # The cover image for the playlist. Uploaded images will be saved in a 'covers/' folder.
    # We use null=True and blank=True so it's optional if a student doesn't have an image ready.
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    
    # The date and time when this playlist was created. It automatically sets to the current time when created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This function helps to display the name of the playlist instead of "Playlist object (1)" in the admin panel.
    def __str__(self):
        return self.title


# This is our model for Songs. A song belongs to a specific playlist.
class Song(models.Model):
    # ForeignKey links each song to one Playlist.
    # on_delete=models.CASCADE means if a playlist is deleted, all its songs are deleted too.
    # related_name='songs' lets us access a playlist's songs using playlist.songs.all()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='songs')
    
    # The title of the song (e.g. "Stairway to Heaven")
    title = models.CharField(max_length=150)
    
    # The artist of the song (optional)
    artist = models.CharField(max_length=100, blank=True, null=True)
    
    # The audio track file. Uploaded audio will be saved in a 'songs/' folder.
    audio_file = models.FileField(upload_to='songs/')
    
    # The song cover poster image (optional)
    song_image = models.ImageField(upload_to='song_covers/', blank=True, null=True)
    
    # Date when the song was added
    created_at = models.DateTimeField(auto_now_add=True)

    # This function shows "Song Title by Artist" in the admin dashboard.
    def __str__(self):
        if self.artist:
            return f"{self.title} by {self.artist}"
        return self.title
