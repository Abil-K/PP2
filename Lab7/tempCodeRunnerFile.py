

def play_next_song():
    global currently_playing_song
    currently_playing_song = (currently_playing_song + 1) % len(songs)