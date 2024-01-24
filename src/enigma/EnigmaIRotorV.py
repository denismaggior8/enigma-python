from Rotor import Rotor


class EnigmaIRotorV(Rotor):
    
    wiring = 'vzbrgityupsdnhlxawmjqofeck'
    notch_indexes = [25]

    def __init__(self, position):
        super().__init__(self.wiring,position,self.notch_indexes)

