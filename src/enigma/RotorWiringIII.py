from Rotor import Rotor


class RotorWiringIII(Rotor):
    
    wiring = 'bdfhjlcprtxvznyeiwgakmusqo'
    notch_index = 21

    def __init__(self, position):
        super().__init__(self.wiring,position,self.notch_index)

