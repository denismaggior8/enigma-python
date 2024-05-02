from .Rotor import Rotor
from .Reflector import Reflector
class ReflectorUKWB(Reflector):
    
    wiring = 'yruhqsldpxngokmiebfzcwvjat'
    tag = "UKW-B"
    
    def __init__(self):
        super().__init__(self.wiring,0)