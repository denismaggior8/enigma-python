from .Alphabets import Alphabets
from .SettableReflector import SettableReflector

class ReflectorUKW_EnigmaT(SettableReflector):
    
    wiring = 'gekpbtaumocniljdxzyfhwvqsr'
    tag = "UKW-T"
    
    def __init__(self, position=0, ring=0):
        super().__init__(
                            wiring=self.wiring,
                            position=position,
                            ring=ring,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )

