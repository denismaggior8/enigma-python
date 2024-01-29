from Rotor import Rotor


class EnigmaM4RotorGamma(Rotor):
    
    wiring = 'fsokanuerhmbtiycwlqpzxvgjd'
    notch_indexes = []

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

