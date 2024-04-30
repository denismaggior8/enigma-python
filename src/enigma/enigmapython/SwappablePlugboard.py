from .Plugboard import Plugboard
from .PlugboardPassthrough import PlugboardPassthrough

class SwappablePlugboard(PlugboardPassthrough):

    def swap(self, c1,c2):
        self.wiring = self.wiring.replace(c1,c2)
