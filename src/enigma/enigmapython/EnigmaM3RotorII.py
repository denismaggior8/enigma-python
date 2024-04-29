from .Rotor import Rotor
from .EnigmaIRotorII import EnigmaIRotorII

class EnigmaM3RotorII(EnigmaIRotorII):

    tag = "M3_II"

    def __init__(self, position = 0, ring = 0):
        super().__init__(position, ring)
    
