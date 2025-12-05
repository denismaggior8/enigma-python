from .Reflector import Reflector
from .Settable import Settable

class SettableReflector(Reflector, Settable):
    def __init__(self, wiring, alphabet, position=0, ring=0):
        Reflector.__init__(self, wiring=wiring, alphabet=alphabet)
        Settable.__init__(self, position=position, ring=ring)
        self.set_ring(self.ring)
