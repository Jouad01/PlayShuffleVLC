from attr import validate
from src.check_play_shuffle import check_play_shuffle
import pytest

valida1 = { 0:"allthat.mp3",
            1:"groovy.mp3",
            2:"moose.mp3"
        }

valida2 = { 2:"allthat.mp3",
            1:"groovy.mp3",
            3:"moose.mp3"
        }

valida3 = { 0:"moose.mp3",
            1:"groovy.mp3",
            2:"allthat.mp3"
        }

erronea1 = { 0:"allthat.mp3",
             1:"allthat.mp3",
             2:"moose.mp3"
        }

erronea2 = { 0:"allthat.mp3",
             1:"allthat.mp3",
             2:"allthat.mp3"
        }

erronea3 = { 0:"allthat.mp3",
             1:"moose.mp3",
             2:"moose.mp3"
        }

@pytest.mark.check_play_shuffle
def test_check_play_shuffle():
    assert check_play_shuffle(valida1) == True
    assert check_play_shuffle(erronea1) == False
    assert check_play_shuffle(erronea2) == False
    assert check_play_shuffle(valida2) == True
    assert check_play_shuffle(valida3) == True
    assert check_play_shuffle(erronea3) == False

