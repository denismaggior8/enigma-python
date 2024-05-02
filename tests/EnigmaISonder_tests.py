from enigmapython.EnigmaISonderRotorI import EnigmaISonderRotorI
from enigmapython.EnigmaISonderRotorII import EnigmaISonderRotorII
from enigmapython.EnigmaISonderRotorIII import EnigmaISonderRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorSonderUKW import ReflectorSonderUKW
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaISonder import EnigmaISonder
from enigma.machine import EnigmaMachine
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaISonder(unittest.TestCase):

     def test_enigma_3_rotors_I_II_III_sonder(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaISonderRotorI(0)
        rotor2 = EnigmaISonderRotorII(0)
        rotor3 = EnigmaISonderRotorIII(0)
        reflector = ReflectorSonderUKW()
        etw = EtwPassthrough()
        enigma = EnigmaISonder(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "supercalifragilistichespiralidoso"
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"fwudwasqpchevhifooqyvvanphhgcfwoa","Enigma encryption error")
     
        

if __name__ == "__main__":
    unittest.main(verbosity=2)