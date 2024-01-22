from .Rotor import Rotor

class RotorWiringIII(Rotor):
    
    wiring = 'bdfhjlcprtxvznyeiwgakmusqo'
    
    def __init__(self, position):
        super().__init__(self.wiring,position)