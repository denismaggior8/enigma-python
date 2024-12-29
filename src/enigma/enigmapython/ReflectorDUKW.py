from .Reflector import Reflector
from .Alphabets import Alphabets    
class ReflectorDUKW(Reflector):
    
    wiring = 'imetcgfraysqbzxwlhkdvupojn'
    tag = "D_UKW"
    
    def __init__(self):
        super().__init__(
                            wiring=self.wiring,
                            ring=0,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )