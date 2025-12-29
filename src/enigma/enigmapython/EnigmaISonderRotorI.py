from .Rotor import Rotor
from .Alphabets import Alphabets

class EnigmaISonderRotorI(Rotor):
    
    wiring = 'veosirzujdqckgwypnxaflthmb'
    turnover_indexes = [16]
    tag = "IS_I"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
    
