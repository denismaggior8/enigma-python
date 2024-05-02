from .Rotor import Rotor
from .Reflector import Reflector

class ReflectorUKWC(Reflector):
    
    wiring = 'fvpjiaoyedrzxwgctkuqsbnmhl'
    tag = "UKW-C"
    
    def __init__(self):
        super().__init__(self.wiring,0)