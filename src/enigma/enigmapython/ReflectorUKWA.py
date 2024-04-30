from .Rotor import Rotor
from .Reflector import Reflector
class ReflectorUKWA(Reflector):
    
    wiring = 'ejmzalyxvbwfcrquontspikhgd'
    tag = "UKW-A"
    
    def __init__(self):
        super().__init__(self.wiring,0)