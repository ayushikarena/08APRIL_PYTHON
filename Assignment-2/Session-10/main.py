# main.py

# Import functions from playlist.py
from playlist import add_song, remove_song, display_playlist


# Create an empty playlist
playlist = []


# Task 2: Add three songs
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Playlist after adding songs:")
print(playlist)


# Task 3: Remove Shape of You
remove_song("Shape of You", playlist)

print("\nPlaylist after removing Shape of You:")
print(playlist)


# Task 4: Display playlist with position numbers
display_playlist(playlist)