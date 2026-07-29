from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaTRotorVIII(Rotor):
    
    wiring = 'ymtpnzhwkodajxeluvgcbisfr'
    turnover_indexes = [23, 4, 8, 12, 16]  # X, E, I, M, Q
    tag = "T_VIII"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
