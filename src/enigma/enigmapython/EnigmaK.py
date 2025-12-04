from .Enigma import Enigma
from .PlugboardPassthrough import PlugboardPassthrough

class EnigmaK(Enigma):
    def __init__(self, rotor1, rotor2, rotor3, reflector, etw, auto_increment_rotors=True):
        super().__init__(
            plugboard=PlugboardPassthrough(),
            rotors=[rotor1, rotor2, rotor3],
            reflector=reflector,
            etw=etw,
            auto_increment_rotors=auto_increment_rotors
        )

