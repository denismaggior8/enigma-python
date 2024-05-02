from .Plugboard import Plugboard
from .Utils import Utils
from .PlugboardPassthrough import PlugboardPassthrough

class SwappablePlugboard(PlugboardPassthrough):

    def __init__(self, chars=None):
        super().__init__()
        if chars != None:
            for key, value in chars.items():
                if key != None and self.wiring.__contains__(key) and value != None and self.wiring.__contains__(value):
                    self.swap(key,value)

    def swap(self, c1, c2):
        self.wiring = Utils.swap_chars(self.wiring, c1, c2)
        
