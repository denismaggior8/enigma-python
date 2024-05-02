from .Rotor import Rotor
from .Reflector import Reflector

class ReflectorUKWCThin(Reflector):
    
    wiring = 'rdobjntkvehmlfcwzaxgyipsuq'
    tag = "UKW-CT"
    
    def __init__(self):
        super().__init__(self.wiring,0)