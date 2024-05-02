from .Rotor import Rotor


class EnigmaIRotorV(Rotor):
    
    wiring = 'vzbrgityupsdnhlxawmjqofeck'
    notch_indexes = [25]
    tag = "I_V"

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

