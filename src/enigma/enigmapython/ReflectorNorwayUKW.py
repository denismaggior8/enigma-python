from .Rotor import Rotor
from .Reflector import Reflector
class ReflectorNorwayUKW(Reflector):
    
    wiring = 'mowjypuxndsraibfvlkzgqchet'
    tag = "IN_UKW"
    
    def __init__(self):
        super().__init__(self.wiring,0)