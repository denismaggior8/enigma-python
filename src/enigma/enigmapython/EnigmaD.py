from .Enigma import Enigma
from .PlugboardPassthrough import PlugboardPassthrough


class EnigmaD(Enigma):
   
    def __init__(self,rotor1, rotor2, rotor3,reflector,etw,auto_increment_rotors=False):
         rotors = [rotor1, rotor2, rotor3]
         super().__init__(PlugboardPassthrough(),rotors,reflector,etw,auto_increment_rotors)
