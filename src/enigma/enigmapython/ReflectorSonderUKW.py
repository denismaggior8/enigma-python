from .Alphabets import Alphabets
from .Reflector import Reflector
class ReflectorSonderUKW(Reflector):
    
    wiring = 'ciagsndrbytpzfulvhekoqxwjm'
    tag = "IS_UKW"
    
    def __init__(self):
        super().__init__(
                            wiring=self.wiring,
                            ring=0,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )