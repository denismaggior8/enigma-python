from Rotor import Rotor


class RotorWiringII(Rotor):
    
    wiring = 'ajdksiruxblhwtmcqgznpyfvoe'
    notch_indexes = [4]
    
    def __init__(self, position):
        super().__init__(self.wiring,position,self.notch_indexes)