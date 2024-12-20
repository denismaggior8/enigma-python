
from string import ascii_lowercase

class Etw:
    wiring = None

    def switch_char(self,char,shift):
        return self.wiring[ascii_lowercase.index(char)+shift]

    def __init__(self, wiring):
        self.wiring = wiring

    def __str__(self):
        return self.wiring