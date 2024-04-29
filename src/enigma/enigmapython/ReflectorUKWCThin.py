from .Rotor import Rotor

class ReflectorUKWCThin(Rotor):
    
    wiring = 'rdobjntkvehmlfcwzaxgyipsuq'
    tag = "UKW-CT"
    
    def __init__(self):
        super().__init__(self.wiring,0)