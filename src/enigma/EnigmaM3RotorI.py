from Rotor import Rotor

class EnigmaM3RotorI(Rotor):
    
    wiring = 'ekmflgdqvzntowyhxuspaibrcj'
    notch_indexes = [16]
    
    def __init__(self, position):
        super().__init__(self.wiring, position, self.notch_indexes)
    
