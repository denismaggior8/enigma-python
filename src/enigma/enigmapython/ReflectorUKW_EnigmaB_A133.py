from .Rotor import Rotor
from .Alphabets import Alphabets
from .Reflector import Reflector

class ReflectorUKW_EnigmaB_A133(Reflector):
    
    wiring = 'ldgbäncpskjavfzhxuiårmqöotey'
    tag = "B_A133_UKW"
    
    def __init__(self):
        super().__init__(
                            self.wiring,
                            alphabet=Alphabets.lookup.get("enigma_b_a133_28chars_lowercase")
                        )  