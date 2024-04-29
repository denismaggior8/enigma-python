from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM3RotorIV import EnigmaM3RotorIV
from enigmapython.EnigmaM3RotorV import EnigmaM3RotorV
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.EnigmaM4RotorGamma import EnigmaM4RotorGamma
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM4 import EnigmaM4
from enigma.machine import EnigmaMachine
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaM4(unittest.TestCase):
     
    def test_enigma_4_rotors_output(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM4RotorI(0)
        rotor2 = EnigmaM4RotorII(0)
        rotor3 = EnigmaM4RotorIII(0)
        rotor4 = EnigmaM4RotorBeta(0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
        self.assertEqual(enigma.input_char("c"),"p","Enigma output error")

    def test_enigma_4_rotors_output_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM4RotorI(0)
        rotor2 = EnigmaM4RotorII(0)
        rotor3 = EnigmaM4RotorIII(0)
        rotor4 = EnigmaM4RotorBeta(0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
        self.assertEqual(enigma.input_string("ciaodeniscomeva"),"pqzzcdfzhvdesmn","Enigma output error")

    def test_enigma_4_rotors_beta_very_long_output_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM4RotorI(0)
        rotor2 = EnigmaM4RotorII(0)
        rotor3 = EnigmaM4RotorIII(0)
        rotor4 = EnigmaM4RotorBeta(0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor4, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(1000000))
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III Beta',
            reflector='B-Thin',
            ring_settings=[0, 0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_4_rotors_gamma_very_long_output_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM4RotorI(0)
        rotor2 = EnigmaM4RotorII(0)
        rotor3 = EnigmaM4RotorIII(0)
        rotor4 = EnigmaM4RotorGamma(0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor4, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(1000000))
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III Gamma',
            reflector='B-Thin',
            ring_settings=[0, 0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")


    def test_enigma_4_rotors_ring_settings(self):
        rnd_ring1 = random.randrange(26)
        rnd_ring2 = random.randrange(26)
        rnd_ring3 = random.randrange(26)
        rnd_ring4 = random.randrange(26)
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM4RotorI(0,rnd_ring1)
        rotor2 = EnigmaM4RotorII(0,rnd_ring2)
        rotor3 = EnigmaM4RotorIII(0,rnd_ring3)
        rotor4 = EnigmaM4RotorGamma(0,rnd_ring4)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor4, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III Gamma',
            reflector='B-Thin',
            ring_settings=[rnd_ring1, rnd_ring2, rnd_ring3, rnd_ring4],
            plugboard_settings=None)
        other_machine.set_display('AAAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    
if __name__ == "__main__":
    unittest.main(verbosity=2)