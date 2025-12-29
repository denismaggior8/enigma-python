import unittest
from enigmapython.EnigmaKRotorI import EnigmaKRotorI
from enigmapython.EnigmaKRotorII import EnigmaKRotorII
from enigmapython.EnigmaKRotorIII import EnigmaKRotorIII
from enigmapython.ReflectorUKW_EnigmaCommercial import ReflectorUKW_EnigmaCommercial
from enigmapython.EtwQWERTZ import EtwQWERTZ
from enigmapython.EnigmaK import EnigmaK

class TestEnigmaK(unittest.TestCase):
    def test_encryption_decryption(self):
        """Test that Enigma K can encrypt and decrypt a message"""
        # Setup
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)
        
        # Encrypt
        plaintext = "helloworld"
        ciphertext = enigma.input_string(plaintext)
        
        # Reset rotors
        rotor1.set_position(0)
        rotor2.set_position(0)
        rotor3.set_position(0)
        
        # Decrypt
        decrypted = enigma.input_string(ciphertext)
        
        self.assertEqual(decrypted, plaintext)
    
    def test_no_plugboard(self):
        """Test that Enigma K uses PlugboardPassthrough (no actual plugboard)"""
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)
        
        # Verify plugboard exists but is passthrough
        self.assertIsNotNone(enigma.plugboard)
        self.assertEqual(enigma.plugboard.__class__.__name__, 'PlugboardPassthrough')
    
    def test_three_rotors(self):
        """Test that Enigma K has exactly 3 rotors"""
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)
        
        self.assertEqual(len(enigma.rotors), 3)
    
    def test_rotor_stepping(self):
        """Test that rotors step correctly"""
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)
        
        initial_pos = enigma.rotors[0].position
        enigma.input_char('a')
        
        # Right rotor should have stepped
        self.assertEqual(enigma.rotors[0].position, initial_pos + 1)
    
    def test_verified_vector(self):
        """
        Test against a vector verified with dencode.com and cryptii.com
        Settings:
            - Rotors: I-II-III
            - Ring Settings: A-A-A (0-0-0)
            - Initial Positions: A-A-A (0-0-0)
            - Reflector: UKW (Commercial)
            - ETW: QWERTZ
        """
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)
        
        plaintext = "helloworld"
        expected_ciphertext = "acsyipzuuu"
        
        ciphertext = enigma.input_string(plaintext)
        self.assertEqual(ciphertext, expected_ciphertext)
    
    def test_dynamic_notch_with_ring_settings(self):
        """
        Test Enigma K with non-zero ring settings to verify DynamicNotchRotor behavior.
        Settings:
            - Rotors: I-II-III (Fast-Middle-Slow)
            - Ring Settings: K-D-N (10-3-13)
            - Initial Positions: A-A-A (0-0-0)
            - Reflector: UKW (Commercial)
            - ETW: QWERTZ
        """
        rotor_fast = EnigmaKRotorI(position=0, ring=10)
        rotor_middle = EnigmaKRotorII(position=0, ring=3)
        rotor_slow = EnigmaKRotorIII(position=0, ring=13)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor_fast, rotor_middle, rotor_slow, reflector, etw, True)
        
        plaintext = "supercalifragilistichespiralidoso"
        ciphertext = enigma.input_string(plaintext)
        
        # This test verifies that the implementation produces consistent output
        # with the dynamic notch behavior (notch position affected by ring setting)
        self.assertIsNotNone(ciphertext)
        self.assertEqual(len(ciphertext), len(plaintext))

        expected_ciphertext = "wjcviwotfjiyycdnqrsoocbqfsurwjaew"
        self.assertEqual(ciphertext, expected_ciphertext)

if __name__ == '__main__':
    unittest.main()
