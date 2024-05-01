from .Plugboard import Plugboard
from .Utils import Utils
from .PlugboardPassthrough import PlugboardPassthrough

class SwappablePlugboard(PlugboardPassthrough):

    def __init__(self,c1=None,c2=None):
        super().__init__()
        if c1 != None and self.wiring.__contains__(c1) and c2 != None and self.wiring.__contains__(c2):
            self.swap(c1,c2)

    def swap(self, c1, c2):
        self.wiring = Utils.swap_chars(self.wiring, c1, c2)
        
