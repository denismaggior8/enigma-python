from enigmapython.EnigmaIRotorI import EnigmaIRotorI
from enigmapython.EnigmaIRotorII import EnigmaIRotorII
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKWB import ReflectorUKWB
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
        rotor1.set_rotor_ring(1)
        rotor2.set_rotor_ring(20)
        rotor3.set_rotor_ring(8)
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
        

if __name__ == "__main__":
    unittest.main(verbosity=2)