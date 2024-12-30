
from .Alphabets import Alphabets
from .Scrambler import Scrambler    

class Etw(Scrambler):
    wiring = None
    alphabet_list = None
    
    def __init__(self, wiring, alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")):
        super().__init__(
            alphabet=alphabet,
            ring=0,
            wiring=wiring
        )
        self.wiring = wiring
        self.alphabet_list = list(alphabet)

    def __str__(self):
        return self.wiring