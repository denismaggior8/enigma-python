from .Rotor import Rotor

class RotorWiringI(Rotor):
    
    wiring = 'ekmflgdqvzntowyhxuspaibrcj'
    
    def __init__(self, position):
        super().__init__(self.wiring, position)