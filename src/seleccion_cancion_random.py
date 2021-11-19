import random

libreria = {"allthat":
                {"track-number": 3, "artist": "unknown", "album": "unknown", "location": "../songs/allthat.mp3"},
            "groovy": 
                {"track-number": 1, "artist": "unknown", "album": "unknown", "location": "../songs/groovy.mp3"},
            "moose":
                {"track-number": 3, "artist": "unknown", "album": "unknown", "location": "../songs/moose.mp3"}   
            }

def seleccion_cancion_random(libreria):
    
    # seleccionamos una cancion aleatoria de la lista de las claves de la libreria
    cancion = random.choice(list(libreria.keys()))

    return str(cancion)
