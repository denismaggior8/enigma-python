from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaTRotorIII(Rotor):
    
    wiring = 'qudlyrfekonvzaxwhmgpjbsict'
    turnover_indexes = [22, 25, 4, 10, 16]  # W, Z, E, K, Q
    tag = "T_III"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
