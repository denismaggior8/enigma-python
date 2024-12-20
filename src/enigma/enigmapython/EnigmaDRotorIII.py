from .Rotor import Rotor

class EnigmaDRotorIII(Rotor):
    
    wiring = 'cjgdpshkturawzxfmynqobvlie'
    notch_indexes = [13]
    tag = "D_III"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
