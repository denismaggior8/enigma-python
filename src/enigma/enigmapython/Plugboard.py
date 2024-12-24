
from string import ascii_lowercase

class Plugboard:
    wiring = None
    alphabet = None

    def switch_char(self,char):
        alphabet = list(ascii_lowercase)
        return self.wiring[alphabet.index(char)]

    def __init__(self, wiring, alphabet=ascii_lowercase):
        self.wiring = wiring
        self.alphabet = alphabet

    def __str__(self):
        return self.wiring