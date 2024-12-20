from .Rotor import Rotor
from .Reflector import Reflector
class ReflectorDUKW(Reflector):
    
    wiring = 'imetcgfraysqbzxwlhkdvupojn'
    tag = "D_UKW"
    
    def __init__(self):
        super().__init__(self.wiring,0)