from Rotor import Rotor


class EnigmaINorwayRotorII(Rotor):
    
    wiring = 'gjlpubswemctqvhxaofzdrkyni'
    notch_indexes = [4]
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)