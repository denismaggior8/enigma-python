from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII
from enigmapython.EnigmaM3RotorIV import EnigmaM3RotorIV
from enigmapython.EnigmaM3RotorV import EnigmaM3RotorV
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM3 import EnigmaM3

from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestClonable(unittest.TestCase):

    def test_clone_enigma_register_observer(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        new_enigma = enigma.clone()
        for _ in range(25):
            new_enigma.input_char('a')
        self.assertEqual(new_enigma.rotors[1].position,1,"Rotor 1 is still at position 0")

if __name__ == "__main__":
    unittest.main()