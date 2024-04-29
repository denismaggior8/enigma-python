from .Rotor import Rotor


class EnigmaISonderRotorII(Rotor):
    
    #wiring = 'uemoatqlshpkcyfwjzbgvxindr'
    wiring = 'uemoatqlshpkcyfwjzbgvxidnr'
    notch_indexes = [4]
    tag = "IS_II"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)