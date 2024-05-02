from .Rotor import Rotor

class EnigmaIRotorIII(Rotor):
    
    wiring = 'bdfhjlcprtxvznyeiwgakmusqo'
    notch_indexes = [21]
    tag = "I_III"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
