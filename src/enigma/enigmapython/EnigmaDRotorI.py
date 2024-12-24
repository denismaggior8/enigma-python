from .Rotor import Rotor

class EnigmaDRotorI(Rotor):
    
    wiring = 'lpgszmhaeoqkvxrfybutnicjdw'
    notch_indexes = [24]
    tag = "D_I"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
