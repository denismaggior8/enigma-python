from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaB_A133RotorIII(Rotor):
    
    wiring = 'åvqiaäxrjbözspcfyunthdomekgl'
    notch_indexes = [5]
    tag = "B_A133_III"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(self.wiring, position, ring, self.notch_indexes, alphabet=Alphabets.lookup.get("enigma_b_a133_28chars_lowercase"))
    
