from .Rotor import Rotor
from .Reflector import Reflector
from .Alphabets import Alphabets
from .RotatingReflector import RotatingReflector


class ReflectorUKW_EnigmaZ(RotatingReflector):
    
    wiring = '5079183642'
    turnover_indexes = [3]
    tag = "Z_UKW"
    
    def __init__(self):
        super().__init__(
                            self.wiring,
                            ring=0,
                            turnover_indexes=self.turnover_indexes,
                            alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers")
                        )