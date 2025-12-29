from .DynamicTurnoverRotor import DynamicTurnoverRotor
from .Alphabets import Alphabets

class EnigmaDRotorII(DynamicTurnoverRotor):
    
    wiring = 'slvgbtfxjqohewirzyamkpcndu'
    turnover_indexes = [25]
    tag = "D_II"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring=self.wiring, 
                            position=position, 
                            ring=ring, 
                            turnover_indexes=self.turnover_indexes,
                            alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase'),
                            turnover_function=lambda n, r, l: (n + r) % l
                        )
    
