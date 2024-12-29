from .Rotor import Rotor


class EnigmaIRotorIV(Rotor):
    
    wiring = 'esovpzjayquirhxlnftgkdcmwb'
    notch_indexes = [9]
    
    tag = "I_IV"

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

