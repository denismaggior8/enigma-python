import unittest
from enigmapython.EnigmaKSwissRotorI import EnigmaKSwissRotorI
from enigmapython.EnigmaKSwissRotorII import EnigmaKSwissRotorII
from enigmapython.EnigmaKSwissRotorIII import EnigmaKSwissRotorIII
from enigmapython.ReflectorUKW_EnigmaCommercial import ReflectorUKW_EnigmaCommercial
from enigmapython.EtwQWERTZ import EtwQWERTZ
from enigmapython.EnigmaKSwiss import EnigmaKSwiss

class TestEnigmaKSwiss(unittest.TestCase):
    
    def test_helloworld_encryption(self):
        """
        Test against a known ciphertext for Enigma K Swiss.
        Settings:
            - Rotors: Swiss I-II-III
            - Ring Settings: A-A-A (0-0-0)
            - Initial Positions: A-A-A (0-0-0)
            - Reflector: UKW (Commercial)
            - ETW: QWERTZ
        """
        rotor1 = EnigmaKSwissRotorI(0, 0)
        rotor2 = EnigmaKSwissRotorII(0, 0)
        rotor3 = EnigmaKSwissRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaKSwiss(rotor1, rotor2, rotor3, reflector, etw, True)
        
        plaintext = "helloworld"
        expected_ciphertext = "xtkxeisfuq"
        
        ciphertext = enigma.input_string(plaintext)
        self.assertEqual(ciphertext, expected_ciphertext)
        
        # Test decryption
        rotor1.set_position(0)
        rotor2.set_position(0)
        rotor3.set_position(0)
        
        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, plaintext)

    def test_helloworld_encryption_ring_1(self):
        """
        Test against a known ciphertext for Enigma K Swiss with ring settings.
        Settings:
            - Rotors: Swiss I-II-III
            - Ring Settings: B-B-B (1-1-1)
            - Initial Positions: A-A-A (0-0-0)
            - Reflector: UKW (Commercial)
            - ETW: QWERTZ
        """
        rotor1 = EnigmaKSwissRotorI(position=0, ring=1)
        rotor2 = EnigmaKSwissRotorII(position=0, ring=1)
        rotor3 = EnigmaKSwissRotorIII(position=0, ring=1)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaKSwiss(rotor1, rotor2, rotor3, reflector, etw, True)
        
        plaintext = "helloworld"
        expected_ciphertext = "dnisfgapiv"
        
        ciphertext = enigma.input_string(plaintext)
        self.assertEqual(ciphertext, expected_ciphertext)
        
        # Test decryption
        rotor1.set_position(0)
        rotor2.set_position(0)
        rotor3.set_position(0)
        
        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, plaintext)

if __name__ == '__main__':
    unittest.main()
