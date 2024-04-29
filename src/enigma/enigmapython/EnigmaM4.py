from .Enigma import Enigma


class EnigmaM4(Enigma):
   
    def __init__(self, plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, auto_increment_rotors=False):
         rotors = [rotor1, rotor2, rotor3, rotor4]
         super().__init__(plugboard,rotors,reflector,etw,auto_increment_rotors)
