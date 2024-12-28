from .Etw import Etw
from .Alphabets import Alphabets

class EnigmaZEtw(Etw):
    wiring = "1234567890"
    def __init__(self):
         super().__init__(self.wiring,alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers"))