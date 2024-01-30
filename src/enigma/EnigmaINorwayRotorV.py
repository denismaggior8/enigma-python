from Rotor import Rotor


class EnigmaINorwayRotorV(Rotor):
    
    wiring = 'hejxqotzbvfdascilwpgynmurk'
    notch_indexes = [25]

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

