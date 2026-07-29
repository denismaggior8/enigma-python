from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaTRotorIV(Rotor):
    
    wiring = 'ciwtbkxnrespflydagvhuojzm'
    turnover_indexes = [22, 25, 5, 11, 17]  # W, Z, F, L, R
    tag = "T_IV"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
