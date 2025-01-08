from .Etw import Etw
from .Alphabets import Alphabets

class EnigmaB_A133Etw(Etw):
    wiring = "abcdefghijklmnopqrstuvxyzåäö"
    def __init__(self):
         super().__init__(self.wiring, alphabet=Alphabets.lookup.get("enigma_b_a133_28chars_lowercase"))