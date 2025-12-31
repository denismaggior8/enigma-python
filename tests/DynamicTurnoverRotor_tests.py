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
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=0)
        self.assertEqual(rotor.turnover_indexes, [25], "Notch should be at original position with ring 0")
        
        # ring = 1 (B)
        # Formula: (25 + 1) % 26 = 0
        rotor.set_ring(1)
        self.assertEqual(rotor.turnover_indexes, [0], "Notch should move forward by 1 with ring 1")
        
        # ring = 5 (F)
        # Formula: (25 + 5) % 26 = 4
        rotor.set_ring(5)
        self.assertEqual(rotor.turnover_indexes, [4], "Notch should move forward by 5 with ring 5")
        
        # ring = 26 (A again, effectively 0)
        rotor.set_ring(26)
        self.assertEqual(rotor.turnover_indexes, [25], "Notch should return to original with ring 26/0")

    def test_init_with_ring(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [10] 
        
        # Init with ring 5
        # Expected: (10 + 5) % 26 = 15
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=5)
        self.assertEqual(rotor.turnover_indexes, [15], "Notch should be adjusted during init")

    def test_multiple_notches(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [0, 13] # A and N
        
        # Ring 1
        # 0 -> (0+1)%26 = 1
        # 13 -> (13+1)%26 = 14
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=1)
        self.assertEqual(rotor.turnover_indexes, [1, 14])

    def test_custom_turnover_function(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [10]
        
        # Define a custom turnover function: (notch - ring) % length
        custom_func = lambda notch, ring, length: (notch - ring) % length
        
        # Ring = 2
        # Expected: (10 - 2) % 26 = 8
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=2, turnover_function=custom_func)
        self.assertEqual(rotor.turnover_indexes, [8], "Custom turnover function should subtract ring setting")
        
        # Define slightly more complex function: (notch * ring) % length
        # Ring = 3
        # Expected: (10 * 3) % 26 = 30 % 26 = 4
        custom_func_2 = lambda notch, ring, length: (notch * ring) % length
        rotor_2 = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=3, turnover_function=custom_func_2)
        self.assertEqual(rotor_2.turnover_indexes, [4], "Custom turnover function should multiply")

    def test_ring_property(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [10] # K
        
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=0)
        self.assertEqual(rotor.turnover_indexes, [10])
        
        # Setting ring via property should trigger set_ring and update turnover_indexes
        rotor.ring = 5
        self.assertEqual(rotor.ring, 5)
        self.assertEqual(rotor.turnover_indexes, [15], "Setting .ring property should update turnover_indexes")

    def test_reset_ring(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [10]
        
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=5)
        self.assertEqual(rotor.turnover_indexes, [15])
        
        rotor.reset_ring()
        self.assertEqual(rotor.ring, 0)
        self.assertEqual(rotor.turnover_indexes, [10], "reset_ring should return turnover_indexes to original values")

    def test_reset_ring_with_custom_function(self):
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
        wiring = alphabet
        original_notches = [10]
        custom_func = lambda notch, ring, length: (notch + 2*ring) % length
        
        rotor = DynamicTurnoverRotor(wiring=wiring, turnover_indexes=original_notches, alphabet=alphabet, position=0, ring=5, turnover_function=custom_func)
        # (10 + 2*5) % 26 = 20
        self.assertEqual(rotor.turnover_indexes, [20])
        
        rotor.reset_ring()
        self.assertEqual(rotor.ring, 0)
        self.assertEqual(rotor.turnover_indexes, [10], "reset_ring should return turnover_indexes to original values even with custom function")

if __name__ == "__main__":
    unittest.main()
