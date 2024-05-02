from .Rotor import Rotor


class EnigmaINorwayRotorIV(Rotor):
    
    wiring = 'fgzjmvxepbwshqtliudykcnrao'
    notch_indexes = [21]
    tag = "IN_IV"

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

