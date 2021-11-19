# se testea que las canciones selecciondas sean de la libreria

from src.seleccion_cancion_random import seleccion_cancion_random
from src.seleccion_cancion_random import libreria
from src.check_seleccion_cancion_random import check_seleccion_cancion_random
import pytest

canciones_invalidas = ['godzilla', 'butterfly effect', 'monster', 'waka waka']

@pytest.mark.seleccion_cancion_random
def test_seleccion_cancion_random():
    
    for cancion in canciones_invalidas:
        
        # seleccion de unas cuantas canciones aleatorias de la libreria
        assert check_seleccion_cancion_random(libreria, seleccion_cancion_random(libreria)) == True
        assert check_seleccion_cancion_random(libreria, seleccion_cancion_random(libreria)) == True
        assert check_seleccion_cancion_random(libreria, seleccion_cancion_random(libreria)) == True

        # seleccion de canciones que no estan en la libreria
        assert check_seleccion_cancion_random(libreria, cancion) == False