from .Reflector import Reflector
from .Alphabets import Alphabets

class ReflectorUKW_EnigmaCommercial(Reflector):
    """Shared UKW reflector used by commercial Enigma D and Enigma K"""
    
    wiring = 'imetcgfraysqbzxwlhkdvupojn'
    
    def __init__(self):
        super().__init__(
            wiring=self.wiring,
            ring=0,
            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        )
