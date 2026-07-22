from django.contrib import admin
from .models import Playlist, Song  # Import the new Song model

# This allows us to add songs directly inside the Playlist page in the admin panel.
# "TabularInline" displays the songs in a clean table format.
class SongInline(admin.TabularInline):
    model = Song
    extra = 1  # Shows 1 empty row by default to add a song

# We customize the Playlist admin view to include the inline Song editor.
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [SongInline]  # Embeds the song form directly inside the playlist form

# Registering models with custom Admin settings
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song)  # Also register Song separately in case we want to view all songs
