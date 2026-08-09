# playlist.py

# Task 1: Add a song
def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist


# Task 3: Remove a song
def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    else:
        print(song_name, "was not found in the playlist")

    return playlist


# Task 4: Display playlist
def display_playlist(playlist):
    print("\nMy Playlist:")

    for position, song in enumerate(playlist, start=1):
        print(position, "-", song)