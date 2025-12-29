import unittest
from enigmapython.DynamicTurnoverRotor import DynamicTurnoverRotor
from enigmapython.Alphabets import Alphabets

class TestDynamicTurnoverRotor(unittest.TestCase):

    def test_notch_movement_with_ring_setting(self):
        # Setup basic rotor parameters
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet # Identity wiring for simplicity
        original_notches = [25] # Notch at Z (index 25)
        
        # ring = 0
        rotor = DynamicTurnoverRotor(wiring=wiring, notch_indexes=original_notches, alphabet=alphabet, position=0, ring=0)
        self.assertEqual(rotor.notch_indexes, [25], "Notch should be at original position with ring 0")
        
        # ring = 1 (B)
        # Formula: (25 + 1) % 26 = 0
        rotor.set_ring(1)
        self.assertEqual(rotor.notch_indexes, [0], "Notch should move forward by 1 with ring 1")
        
        # ring = 5 (F)
        # Formula: (25 + 5) % 26 = 4
        rotor.set_ring(5)
        self.assertEqual(rotor.notch_indexes, [4], "Notch should move forward by 5 with ring 5")
        
        # ring = 26 (A again, effectively 0)
        rotor.set_ring(26)
        self.assertEqual(rotor.notch_indexes, [25], "Notch should return to original with ring 26/0")

    def test_init_with_ring(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [10] 
        
        # Init with ring 5
        # Expected: (10 + 5) % 26 = 15
        rotor = DynamicTurnoverRotor(wiring=wiring, notch_indexes=original_notches, alphabet=alphabet, position=0, ring=5)
        self.assertEqual(rotor.notch_indexes, [15], "Notch should be adjusted during init")

    def test_multiple_notches(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [0, 13] # A and N
        
        # Ring 1
        # 0 -> (0+1)%26 = 1
        # 13 -> (13+1)%26 = 14
        rotor = DynamicTurnoverRotor(wiring=wiring, notch_indexes=original_notches, alphabet=alphabet, position=0, ring=1)
        self.assertEqual(rotor.notch_indexes, [1, 14])

if __name__ == "__main__":
    unittest.main()
