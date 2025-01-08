from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaB_A133RotorII(Rotor):
    
    wiring = 'chnsyöadmotrzxbäigåekqupflvj'
    notch_indexes = [15]
    tag = "B_A133_II"

    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring=self.wiring, 
                            position=position, 
                            ring=ring, 
                            notch_indexes=self.notch_indexes, 
                            alphabet=Alphabets.lookup.get("enigma_b_a133_28chars_lowercase")
                        )
    
