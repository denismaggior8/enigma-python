from .Rotor import Rotor
from .EnigmaM3RotorII import EnigmaM3RotorII

class EnigmaM4RotorII(EnigmaM3RotorII):

    tag = "M4_II"

    def __init__(self, position = 0, ring = 0):
        super().__init__(position, ring)
    
