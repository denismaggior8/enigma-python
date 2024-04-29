from .Rotor import Rotor

class EnigmaIRotorII(Rotor):
    
    wiring = 'ajdksiruxblhwtmcqgznpyfvoe'
    notch_indexes = [4]
    tag = "I_II"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
