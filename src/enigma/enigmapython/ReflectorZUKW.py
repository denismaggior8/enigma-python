from .Rotor import Rotor
from .Reflector import Reflector
from .Alphabets import Alphabets

class ReflectorZUKW(Reflector):
    
    wiring = '5079183642'
    tag = "D_UKW"
    
    def __init__(self):
        super().__init__(self.wiring,0,alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers"))