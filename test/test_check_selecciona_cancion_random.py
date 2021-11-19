from src.check_seleccion_cancion_random import check_seleccion_cancion_random
import pytest
from src.check_seleccion_cancion_random import libreria


@pytest.mark.check_cancion_random
def test_check_cancion_random():
    assert check_seleccion_cancion_random(libreria, "no está en la libreria") == False
    assert check_seleccion_cancion_random(libreria, "groovy") == True
    assert check_seleccion_cancion_random(libreria, "allthat") == True
    assert check_seleccion_cancion_random(libreria, "moose") == True
    assert check_seleccion_cancion_random(libreria, "tampoco está") == False
