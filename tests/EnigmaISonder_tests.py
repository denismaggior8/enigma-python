from EnigmaISonderRotorI import EnigmaISonderRotorI
from EnigmaISonderRotorII import EnigmaISonderRotorII
from EnigmaISonderRotorIII import EnigmaISonderRotorIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorSonderUKW import ReflectorSonderUKW
from EtwPassthrough import EtwPassthrough
from EnigmaISonder import EnigmaISonder
from enigma.machine import EnigmaMachine
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaISonder(unittest.TestCase):
     
     def test_enigma_3_rotors_I_II_III_sonder_simple_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaISonderRotorI(0)
        rotor2 = EnigmaISonderRotorII(0)
        rotor3 = EnigmaISonderRotorIII(0)
        reflector = ReflectorSonderUKW()
        etw = EtwPassthrough()
        enigma = EnigmaISonder(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "a"
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"z","Enigma encryption error")

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
        self.assertEqual(my_encrypted_string,"fwcdwasqpchhvcirooqyvpanphhgcfsoa","Enigma encryption error")
     
        

if __name__ == "__main__":
    unittest.main(verbosity=2)