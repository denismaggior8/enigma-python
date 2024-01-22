
from string import ascii_lowercase

class Plugboard:
    wiring = None

    def switch_char(self,char):
        alphabet = list(ascii_lowercase)
        return self.wiring[alphabet.index(char)]

    def __init__(self, wiring):
        self.wiring = wiring

    def __str__(self):
        return self.wiring