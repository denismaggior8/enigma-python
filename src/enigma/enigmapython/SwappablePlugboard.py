from .Plugboard import Plugboard
from .Utils import Utils
from .Alphabets import Alphabets

class SwappablePlugboard(Plugboard):

    def __init__(self, chars=None, wiring=Alphabets.lookup.get('latin_i18n_26chars_lowercase'), alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase')):
        super().__init__(wiring,alphabet)
        self.bulk_swap(chars)

    def bulk_swap(self,chars):
        if chars != None and isinstance(chars, dict):
            for key, value in chars.items():
                self.swap(key,value)

    def swap(self, c1, c2):
        if c1 != None and self.wiring.__contains__(c1) and c2 != None and self.wiring.__contains__(c2):
            self.wiring = Utils.swap_chars(self.wiring, c1, c2)
        
