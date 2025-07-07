from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.EnigmaM4RotorGamma import EnigmaM4RotorGamma
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.ReflectorUKWC import ReflectorUKWC
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.ReflectorUKWCThin import ReflectorUKWCThin
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM4 import EnigmaM4
from enigmapython.EnigmaM3 import EnigmaM3
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
    
    def test_enigma_4_rotors_ring_settings_swappable_plugboard(self):
        rnd_ring1 = random.randrange(26)
        rnd_ring2 = random.randrange(26)
        rnd_ring3 = random.randrange(26)
        rnd_ring4 = random.randrange(26)
        plugboard = SwappablePlugboard()
        plugboard.swap("d","s")
        rotor1 = EnigmaM4RotorI(0,rnd_ring1)
        rotor2 = EnigmaM4RotorII(0,rnd_ring2)
        rotor3 = EnigmaM4RotorIII(0,rnd_ring3)
        rotor4 = EnigmaM4RotorGamma(0,rnd_ring4)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor4, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(1000000))
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III Gamma',
            reflector='B-Thin',
            ring_settings=[rnd_ring1, rnd_ring2, rnd_ring3, rnd_ring4],
            plugboard_settings="DS")
        other_machine.set_display('AAAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")


    def test_enigma_m4_enigma_m3_beta_compatibility(self):

        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(1000))

        # Enigma M3
        plugboard = PlugboardPassthrough()
        m3Rotor1 = EnigmaM3RotorI(23,0)
        m3Rotor2 = EnigmaM3RotorII(4,0)
        m3Rotor3 = EnigmaM3RotorIII(15,0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigmaM3 = EnigmaM3(plugboard, m3Rotor1, m3Rotor2, m3Rotor3, reflector, etw, True)
        m3_encrypted_string = enigmaM3.input_string(cleartext)

        # Eingma M4
        plugboard = PlugboardPassthrough()
        m4Rotor1 = EnigmaM4RotorI(23,0)
        m4Rotor2 = EnigmaM4RotorII(4,0)
        m4Rotor3 = EnigmaM4RotorIII(15,0)
        m4Rotor4 = EnigmaM4RotorBeta(0,0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigmaM4 = EnigmaM4(plugboard, m4Rotor1, m4Rotor2, m4Rotor3, m4Rotor4, reflector, etw, True)
        m4_encrypted_string = enigmaM4.input_string(cleartext)

        self.assertEqual(m4_encrypted_string,m3_encrypted_string.lower(),"encrypted texts do not match between Enigma M3 and M4")


    def test_enigma_m4_enigma_m3_gamma_compatibility(self):

        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(1000))

        # Enigma M3
        plugboard = PlugboardPassthrough()
        m3Rotor1 = EnigmaM3RotorI(23,0)
        m3Rotor2 = EnigmaM3RotorII(4,0)
        m3Rotor3 = EnigmaM3RotorIII(15,0)
        reflector = ReflectorUKWC()
        etw = EtwPassthrough()
        enigmaM3 = EnigmaM3(plugboard, m3Rotor1, m3Rotor2, m3Rotor3, reflector, etw, True)
        m3_encrypted_string = enigmaM3.input_string(cleartext)

        # Eingma M4
        plugboard = PlugboardPassthrough()
        m4Rotor1 = EnigmaM4RotorI(23,0)
        m4Rotor2 = EnigmaM4RotorII(4,0)
        m4Rotor3 = EnigmaM4RotorIII(15,0)
        m4Rotor4 = EnigmaM4RotorGamma(0,0)
        reflector = ReflectorUKWCThin()
        etw = EtwPassthrough()
        enigmaM4 = EnigmaM4(plugboard, m4Rotor1, m4Rotor2, m4Rotor3, m4Rotor4, reflector, etw, True)
        m4_encrypted_string = enigmaM4.input_string(cleartext)

        self.assertEqual(m4_encrypted_string,m3_encrypted_string.lower(),"encrypted texts do not match between Enigma M3 and M4")

    
if __name__ == "__main__":
    unittest.main(verbosity=2)