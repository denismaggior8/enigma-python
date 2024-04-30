from .Plugboard import Plugboard
from .Utils import Utils
from .PlugboardPassthrough import PlugboardPassthrough

class SwappablePlugboard(PlugboardPassthrough):

    def swap(self, c1, c2):
        self.wiring = Utils.swap_chars(self.wiring, c1, c2)
        
