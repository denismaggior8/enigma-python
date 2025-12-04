from enigmapython.EnigmaINorwayRotorI import EnigmaINorwayRotorI
from enigmapython.EnigmaINorwayRotorII import EnigmaINorwayRotorII
from enigmapython.EnigmaINorwayRotorIII import EnigmaINorwayRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKW_EnigmaINorway import ReflectorUKW_EnigmaINorway
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaINorway import EnigmaINorway
from string import ascii_lowercase
import unittest

class TestEnigmaNorway(unittest.TestCase):

    def test_enigma_3_rotors_I_II_III_norway(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaINorwayRotorI(0)
        rotor2 = EnigmaINorwayRotorII(0)
        rotor3 = EnigmaINorwayRotorIII(0)
        reflector = ReflectorUKW_EnigmaINorway()
        etw = EtwPassthrough()
        enigma = EnigmaINorway(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "supercalifragilistichespiralidoso"
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"mdxaexnvprzuxqpxfzhjxyhdfolomjvmg","Enigma encryption error")
        


if __name__ == "__main__":
    unittest.main(verbosity=2)