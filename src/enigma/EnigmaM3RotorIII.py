from Rotor import Rotor


class EnigmaM3RotorIII(Rotor):
    
    wiring = 'bdfhjlcprtxvznyeiwgakmusqo'
    notch_indexes = [21]

    def __init__(self, position):
        super().__init__(self.wiring,position,self.notch_indexes)
