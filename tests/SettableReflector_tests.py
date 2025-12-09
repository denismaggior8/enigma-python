import unittest
from enigmapython.EnigmaKRotorI import EnigmaKRotorI
from enigmapython.EnigmaKRotorII import EnigmaKRotorII
from enigmapython.EnigmaKRotorIII import EnigmaKRotorIII
from enigmapython.ReflectorUKW_EnigmaCommercial import ReflectorUKW_EnigmaCommercial
from enigmapython.EtwQWERTZ import EtwQWERTZ
from enigmapython.EnigmaK import EnigmaK

class TestSettableReflector(unittest.TestCase):
    def test_reflector_position_affects_output(self):
        """Test that changing reflector position changes the output"""
        # Setup standard Enigma K
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        etw = EtwQWERTZ()
        
        # Reflector at position 0 (default)
        reflector_0 = ReflectorUKW_EnigmaCommercial(position=0)
        enigma_0 = EnigmaK(rotor1, rotor2, rotor3, reflector_0, etw, True)
        
        # Reflector at position 1
        rotor1_b = EnigmaKRotorI(0, 0)
        rotor2_b = EnigmaKRotorII(0, 0)
        rotor3_b = EnigmaKRotorIII(0, 0)
        reflector_1 = ReflectorUKW_EnigmaCommercial(position=1)
        enigma_1 = EnigmaK(rotor1_b, rotor2_b, rotor3_b, reflector_1, etw, True)
        
        plaintext = "aaaaa"
        
        cipher_0 = enigma_0.input_string(plaintext)
        cipher_1 = enigma_1.input_string(plaintext)
        
        print(f"Reflector Pos 0: {cipher_0}")
        print(f"Reflector Pos 1: {cipher_1}")
        
        self.assertNotEqual(cipher_0, cipher_1)

    def test_reflector_is_settable(self):
        """Test that ReflectorUKW_EnigmaCommercial has settable attributes"""
        reflector = ReflectorUKW_EnigmaCommercial()
        self.assertTrue(hasattr(reflector, 'position'))
        self.assertTrue(hasattr(reflector, 'ring'))
        self.assertTrue(hasattr(reflector, 'set_position'))
        
        reflector.set_position(5)
        self.assertEqual(reflector.position, 5)

if __name__ == '__main__':
    unittest.main()
