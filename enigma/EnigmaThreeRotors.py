from .Enigma import Enigma

class EnigmaThreeRotors(Enigma):
   
    def __init__(self,plugboard,rotor1, rotor2, rotor3,reflector,etw):
         rotors = [rotor1, rotor2, rotor3]
         super().__init__(plugboard,rotors,reflector,etw)