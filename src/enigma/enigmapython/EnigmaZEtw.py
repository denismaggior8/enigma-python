from .Etw import Etw
from .Alphabets import Alphabets

class EnigmaZEtw(Etw):
    wiring = Alphabets.lookup.get("enigma_z_10chars_numbers")
    def __init__(self):
         super().__init__(self.wiring,alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers"))