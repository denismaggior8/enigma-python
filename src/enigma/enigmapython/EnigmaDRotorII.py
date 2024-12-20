from .Rotor import Rotor

class EnigmaDRotorII(Rotor):
    
    wiring = 'slvgbtfxjqohewirzyamkpcndu'
    notch_indexes = [4]
    tag = "D_II"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
