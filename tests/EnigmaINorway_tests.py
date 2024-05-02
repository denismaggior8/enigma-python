from enigmapython.EnigmaINorwayRotorI import EnigmaINorwayRotorI
from enigmapython.EnigmaINorwayRotorII import EnigmaINorwayRotorII
from enigmapython.EnigmaINorwayRotorIII import EnigmaINorwayRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorNorwayUKW import ReflectorNorwayUKW
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaINorway import EnigmaINorway
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaNorway(unittest.TestCase):

    def test_enigma_3_rotors_I_II_III_norway(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaINorwayRotorI(0)
        rotor2 = EnigmaINorwayRotorII(0)
        rotor3 = EnigmaINorwayRotorIII(0)
        reflector = ReflectorNorwayUKW()
        etw = EtwPassthrough()
        enigma = EnigmaINorway(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "supercalifragilistichespiralidoso"
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"mdxaexnvprzuxqpxfzhjxyhdfolomjvmg","Enigma encryption error")
        
    #def test_enigma_3_rotors_I_II_III_resetting_rings_rotations_111_very_long_string(self):
    #    plugboard = PlugboardPassthrough()
    #    rotor1 = EnigmaINorwayRotorI(1,4)
    #    rotor2 = EnigmaINorwayRotorII(1,2)
    #    rotor3 = EnigmaINorwayRotorIII(1,6)
    #    rotor1.set_rotor_ring(1)
    #    rotor2.set_rotor_ring(20)
    #    rotor3.set_rotor_ring(8)
    #    reflector = ReflectorNorwayUKW()
    #    etw = EtwPassthrough()
    #    enigma = EnigmaINorway(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
    #    cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
    #    my_encrypted_string = enigma.input_string(cleartext)
    #    self.assertEqual(my_encrypted_string,"","Enigma encryption error")


if __name__ == "__main__":
    unittest.main(verbosity=2)