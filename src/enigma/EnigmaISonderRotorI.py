from Rotor import Rotor

class EnigmaISonderRotorI(Rotor):
    
    wiring = 'veosirzujdqckgwypnxaflthmb'
    notch_indexes = [16]
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes)
    
