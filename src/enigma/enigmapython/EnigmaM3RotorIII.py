from .Rotor import Rotor
from .EnigmaIRotorIII import EnigmaIRotorIII

class EnigmaM3RotorIII(EnigmaIRotorIII):

    tag = "M3_III"

    def __init__(self, position = 0, ring = 0):
        super().__init__(position, ring)
    
