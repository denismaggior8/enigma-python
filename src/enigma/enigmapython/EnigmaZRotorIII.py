from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaZRotorIII(Rotor):
    
    wiring = '3581620794'
    turnover_indexes = [8]
    tag = "Z_III"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers")
                        )
    
