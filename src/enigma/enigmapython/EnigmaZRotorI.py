from .Rotor import Rotor
from .Alphabets import Alphabets 

class EnigmaZRotorI(Rotor):
    
    wiring = '6418270359'
    turnover_indexes = [9]
    tag = "Z_I"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers")
                        )
    
