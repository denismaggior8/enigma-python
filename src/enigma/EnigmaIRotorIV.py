from Rotor import Rotor


class EnigmaIRotorIV(Rotor):
    
    wiring = 'esovpzjayquirhxlnftgkdcmwb'
    notch_indexes = [9]

    def __init__(self, position):
        super().__init__(self.wiring,position,self.notch_indexes)

