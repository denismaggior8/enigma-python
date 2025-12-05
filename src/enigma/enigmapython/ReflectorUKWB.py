from .Alphabets import Alphabets
from .Reflector import Reflector
class ReflectorUKWB(Reflector):
    
    wiring = 'yruhqsldpxngokmiebfzcwvjat'
    tag = "UKW-B"
    
    def __init__(self):
        super().__init__(
                            wiring=self.wiring,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )