from enigmapython.EnigmaIRotorI import EnigmaIRotorI
from enigmapython.EnigmaIRotorII import EnigmaIRotorII
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.ReflectorUKWA import ReflectorUKWA
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaI import EnigmaI
from enigma.machine import EnigmaMachine
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaM3(unittest.TestCase):
     

    def test_enigma_3_rotors_I_II_III_resetting_rings_rotations_111_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaIRotorI(1,4)
        rotor2 = EnigmaIRotorII(1,2)
        rotor3 = EnigmaIRotorIII(1,6)
        rotor1.set_ring(1)
        rotor2.set_ring(20)
        rotor3.set_ring(8)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III',
            reflector='B',
            ring_settings=[1, 20, 8],
            plugboard_settings=None)
        other_machine.set_display('BBB')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_I_II_III_resetting_rings_rotations_111_very_long_string_swappable_plugboard(self):
        plugboard = SwappablePlugboard()
        plugboard.swap("a","z")
        rotor1 = EnigmaIRotorI(1,4)
        rotor2 = EnigmaIRotorII(1,2)
        rotor3 = EnigmaIRotorIII(1,6)
        rotor1.set_ring(1)
        rotor2.set_ring(20)
        rotor3.set_ring(8)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III',
            reflector='B',
            ring_settings=[1, 20, 8],
            plugboard_settings="AZ")
        other_machine.set_display('BBB')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_I_I_I_swappable_plugboard_rotor_a(self):
        plugboard = SwappablePlugboard()
        plugboard.swap("d","z")
        rotor1 = EnigmaIRotorI(0)
        rotor2 = EnigmaIRotorI(0)
        rotor3 = EnigmaIRotorI(0)
        reflector = ReflectorUKWA()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "DENISDENISDENISDENISDENISDENISDENISDENISDENISDENISDENIS".lower()
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"jqoqqwuewdjnccolyagmlaphgrydoprqgocwmeebkhpkbhwujevnzme".lower(),"Enigma encryption error")


    def test_enigma_3_rotors_I_I_I_rotor_1_status_25(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaIRotorI(0)
        rotor2 = EnigmaIRotorI(0)
        rotor3 = EnigmaIRotorI(1)
        reflector = ReflectorUKWA()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ("D" * 24).lower()
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(enigma.rotors[0].position,25,"Enigma rotor position error")

    def test_enigma_3_rotors_I_I_I_rotor_2_status_1(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaIRotorI(0)
        rotor2 = EnigmaIRotorI(0)
        rotor3 = EnigmaIRotorI(1)
        reflector = ReflectorUKWA()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ("D" * 25).lower()
        i_ll_never_use_this = enigma.input_string(cleartext)
        self.assertEqual(enigma.rotors[1].position,1,"Enigma rotor position error")

    def test_enigma_3_rotors_I_I_I_rotor_1_status_9(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaIRotorI(0)
        rotor2 = EnigmaIRotorI(0)
        rotor3 = EnigmaIRotorI(1)
        reflector = ReflectorUKWA()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ("DENISDEN").lower()
        i_ll_never_use_this = enigma.input_string(cleartext)
        self.assertEqual(enigma.rotors[0].position,9,"Enigma rotor position error")

    def test_enigma_3_rotors_I_I_I_rotor_1_status_2_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaIRotorI(1)
        rotor2 = EnigmaIRotorI(0)
        rotor3 = EnigmaIRotorI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ("DENISDEN").lower()
        encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(encrypted_string,"hwhkrpzr","Enigma encryption error")
        self.assertEqual(enigma.rotors[0].position,8,"Enigma rotor position error")
        self.assertEqual(enigma.rotors[2].position,1,"Enigma rotor position error")

if __name__ == "__main__":
    unittest.main(verbosity=2)