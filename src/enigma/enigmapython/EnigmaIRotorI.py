from .Rotor import Rotor

class EnigmaIRotorI(Rotor):
    
    wiring = 'ekmflgdqvzntowyhxuspaibrcj'
    notch_indexes = [16]
    tag = "I_I"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
