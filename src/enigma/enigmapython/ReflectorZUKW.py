from .Rotor import Rotor
from .Reflector import Reflector
from .Alphabets import Alphabets
from .RotatingReflector import RotatingReflector


class ReflectorZUKW(RotatingReflector):
    
    wiring = '5079183642'
    notch_indexes = [3]
    tag = "Z_UKW"
    
    def __init__(self):
        super().__init__(
                            self.wiring,
                            ring=0,
                            notch_indexes=self.notch_indexes,
                            alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers")
                        )