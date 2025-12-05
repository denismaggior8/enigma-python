from .Rotor import Rotor
from .Reflector import Reflector
from .Alphabets import Alphabets

class ReflectorUKWCThin(Reflector):
    
    wiring = 'rdobjntkvehmlfcwzaxgyipsuq'
    tag = "UKW-CT"
    
    def __init__(self):
        super().__init__(
                            wiring=self.wiring,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )