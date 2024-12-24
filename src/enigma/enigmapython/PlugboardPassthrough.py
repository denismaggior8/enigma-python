from .Plugboard import Plugboard
from string import ascii_lowercase

class PlugboardPassthrough(Plugboard):
    wiring = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self,alphabet=ascii_lowercase):
         super().__init__(self.wiring)
