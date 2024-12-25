from .Enigma import Enigma
from .Alphabets import Alphabets
from .PlugboardPassthrough import PlugboardPassthrough


class EnigmaB_A133(Enigma):

    alphabet=Alphabets.lookup.get("enigma_b_a133_28chars_lowercase")

    def __init__(self,rotor1, rotor2, rotor3,reflector,etw,auto_increment_rotors=False):
         rotors = [rotor1, rotor2, rotor3]
         super().__init__(PlugboardPassthrough(alphabet=self.alphabet),rotors,reflector,etw,auto_increment_rotors, alphabet=self.alphabet)  
