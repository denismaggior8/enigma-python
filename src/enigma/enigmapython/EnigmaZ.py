from .Enigma import Enigma
from .Alphabets import Alphabets
from .PlugboardPassthrough import PlugboardPassthrough


class EnigmaZ(Enigma):

    alphabet=Alphabets.lookup.get("enigma_z_10chars_numbers")
   
    def __init__(self,rotor1, rotor2, rotor3,reflector,etw,auto_increment_rotors=False):
         rotors = [rotor1, rotor2, rotor3]
         super().__init__(PlugboardPassthrough(alphabet=self.alphabet),rotors,reflector,etw,auto_increment_rotors,alphabet=self.alphabet)
