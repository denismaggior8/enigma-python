from .Rotor import Rotor


class EnigmaISonderRotorIII(Rotor):
    
    wiring = 'tzhxmbsipnurjfdkeqvcwglaoy'
    notch_indexes = [21]
    tag = "IS_III"

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

