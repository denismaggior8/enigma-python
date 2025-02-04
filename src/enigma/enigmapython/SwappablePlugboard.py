from .Plugboard import Plugboard
from .Alphabets import Alphabets
from .Swappable import Swappable

class SwappablePlugboard(Plugboard,Swappable):

    def __init__(self, chars=None, wiring=Alphabets.lookup.get('latin_i18n_26chars_lowercase'), alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase')):
        super().__init__(wiring,alphabet)
        self.bulk_swap(chars)

        
