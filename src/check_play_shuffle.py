playlist = {0:
            "allthat.mp3",
            1:
            "groovy.mp3",
            2:
            "moose.mp3"
}

def check_play_shuffle(playlist):
    
    # ensure playlist is a dict
    assert isinstance(playlist, dict), "the playlist must be a dictionary"

    # make sure there are not repeated songs
    songs = list(dict.values(playlist))

    for song in songs:
        if songs.count(song) > 1:
            return False
    return True