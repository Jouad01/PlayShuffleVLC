libreria = {"allthat":
                {"track-number": 3, "artist": "unknown", "album": "unknown", "location": "../songs/allthat.mp3"},
            "groovy": 
                {"track-number": 1, "artist": "unknown", "album": "unknown", "location": "../songs/groovy.mp3"},
            "moose":
                {"track-number": 3, "artist": "unknown", "album": "unknown", "location": "../songs/moose.mp3"}   
            }

def check_seleccion_cancion_random(libreria, cancion):
    
    # precondiciones
    assert isinstance(libreria, dict), "la libreria debe ser un diccionario"
    assert isinstance(cancion, str), "la cancion debe ser un string"

    # compruebo si la canción está en la libreria
    if cancion not in libreria:
        return False
    else:
        return True
    