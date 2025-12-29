from .Rotor import Rotor
from .Alphabets import Alphabets


class EnigmaISonderRotorIII(Rotor):
    
    wiring = 'tzhxmbsipnurjfdkeqvcwglaoy'
    turnover_indexes = [21]
    tag = "IS_III"

    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )

