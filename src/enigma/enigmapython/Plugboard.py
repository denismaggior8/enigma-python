
from .Alphabets import Alphabets

class Plugboard:
    wiring = None
    alphabet_list = None

    def switch_char(self,char):
        return self.wiring[self.alphabet_list.index(char)]

    def __init__(self, wiring, alphabet):
        self.wiring = wiring
        self.alphabet_list = list(alphabet)

    def __str__(self):
        return self.wiring