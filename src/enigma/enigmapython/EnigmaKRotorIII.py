from .DynamicNotchRotor import DynamicNotchRotor
from .Alphabets import Alphabets

class EnigmaKRotorIII(DynamicNotchRotor):
    
    wiring = 'cjgdpshkturawzxfmynqobvlie'
    notch_indexes = [13]  # N (position 13)
    tag = "K_III"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            notch_indexes=self.notch_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
    
