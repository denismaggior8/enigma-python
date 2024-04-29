from .Rotor import Rotor

class EnigmaINorwayRotorI(Rotor):
    
    wiring = 'wtokasuyvrbxjhqcpzefmdinlg'
    notch_indexes = [16]
    tag = "IN_I"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
