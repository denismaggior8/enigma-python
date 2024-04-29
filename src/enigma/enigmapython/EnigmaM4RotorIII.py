from .Rotor import Rotor
from .EnigmaM3RotorIII import EnigmaM3RotorIII

class EnigmaM4RotorIII(EnigmaM3RotorIII):

    tag = "M4_III"

    def __init__(self, position = 0, ring = 0):
        super().__init__(position, ring)
    
