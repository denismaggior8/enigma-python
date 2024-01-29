from EnigmaM3RotorI import EnigmaM3RotorI
from EnigmaM3RotorII import EnigmaM3RotorII
from EnigmaM3RotorIII import EnigmaM3RotorIII
from EnigmaM3RotorIV import EnigmaM3RotorIV
from EnigmaM3RotorV import EnigmaM3RotorV
from EnigmaM3RotorVI import EnigmaM3RotorVI
from  EnigmaM4RotorBeta import EnigmaM4RotorBeta
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from ReflectorUKWBThin import ReflectorUKWBThin
from EtwPassthrough import EtwPassthrough
from EnigmaM4 import EnigmaM4
from enigma.machine import EnigmaMachine
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaM4(unittest.TestCase):
     
    def test_enigma_4_rotors_output(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        rotor4 = EnigmaM4RotorBeta(0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
        self.assertEqual(enigma.input_char("c"),"p","Enigma output error")

    
if __name__ == "__main__":
    unittest.main(verbosity=2)