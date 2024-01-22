from .Rotor import Rotor

class RotorWiringII(Rotor):
    
    wiring = 'ajdksiruxblhwtmcqgznpyfvoe'
    
    def __init__(self, position):
        super().__init__(self.wiring,position)