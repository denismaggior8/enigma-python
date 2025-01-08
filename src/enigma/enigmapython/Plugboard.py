
from .Alphabets import Alphabets
from .Scrambler import Scrambler

class Plugboard(Scrambler):
    wiring = None
    alphabet_list = None

    def __init__(self, wiring, alphabet):
        self.wiring = wiring
        self.alphabet_list = list(alphabet)
        super().__init__(
            alphabet=alphabet,
            ring=0,
            wiring=wiring
        )


    def __str__(self):
        return self.wiring