from .Alphabets import Alphabets
from .Reflector import Reflector
class ReflectorUKWBThin(Reflector):
    
    wiring = 'enkqauywjicopblmdxzvfthrgs'
    tag = "UKW-BT"
    
    def __init__(self):
        super().__init__(
                            wiring=self.wiring,
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )