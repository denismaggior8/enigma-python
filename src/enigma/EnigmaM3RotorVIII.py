from Rotor import Rotor


class EnigmaM3RotorVIII(Rotor):
    
    wiring = 'fkqhtlxocbjspdzramewniuygv'
    notch_indexes = [12,25]

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

