from .Rotor import Rotor
from .Reflector import Reflector
from .Alphabets import Alphabets    

class ReflectorUKWC(Reflector):
    
    wiring = 'fvpjiaoyedrzxwgctkuqsbnmhl'
    tag = "UKW-C"
    
    def __init__(self):
        super().__init__(
                            wiring=self.wiring,
                            ring=0,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )