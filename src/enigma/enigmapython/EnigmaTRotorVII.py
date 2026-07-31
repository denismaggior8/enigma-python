from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaTRotorVII(Rotor):
    
    wiring = 'bjvftxplnayozikwgdqeruchsm'
    turnover_indexes = [24, 2, 5, 10, 17]  # Y, C, F, K, R
    tag = "T_VII"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
