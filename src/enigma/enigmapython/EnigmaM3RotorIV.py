from .Rotor import Rotor
from .EnigmaIRotorIV import EnigmaIRotorIV

class EnigmaM3RotorIV(EnigmaIRotorIV):

    tag = "M3_IV"

    def __init__(self, position = 0, ring = 0):
        super().__init__(position, ring)
    
