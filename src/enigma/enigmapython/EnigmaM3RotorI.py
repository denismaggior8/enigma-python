from .Rotor import Rotor
from .EnigmaIRotorI import EnigmaIRotorI

class EnigmaM3RotorI(EnigmaIRotorI):

    tag = "M3_I"

    def __init__(self, position = 0, ring = 0):
        super().__init__(position, ring)
    
