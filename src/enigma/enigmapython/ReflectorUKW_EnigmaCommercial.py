from .SettableReflector import SettableReflector
from .Alphabets import Alphabets

class ReflectorUKW_EnigmaCommercial(SettableReflector):
    """Shared UKW reflector used by commercial Enigma D and Enigma K"""
    
    wiring = 'imetcgfraysqbzxwlhkdvupojn'
    
    def __init__(self, position=0, ring=0):
        super().__init__(
            wiring=self.wiring,
            ring=ring,
            position=position,
            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        )
