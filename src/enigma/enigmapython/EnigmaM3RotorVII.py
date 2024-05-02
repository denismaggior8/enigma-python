from .Rotor import Rotor


class EnigmaM3RotorVII(Rotor):
    
    wiring = 'nzjhgrcxmyswboufaivlpekqdt'
    notch_indexes = [12,25]
    tag = "M3_VII"

    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)

