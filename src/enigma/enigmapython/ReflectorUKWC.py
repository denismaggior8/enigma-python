from .Rotor import Rotor

class ReflectorUKWC(Rotor):
    
    wiring = 'fvpjiaoyedrzxwgctkuqsbnmhl'
    tag = "UKW-C"
    
    def __init__(self):
        super().__init__(self.wiring,0)