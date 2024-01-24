from string import ascii_lowercase
from EnigmaM3RotorII import EnigmaM3RotorII
import unittest

    
class TestEnigmaM3RotorII(unittest.TestCase):
    
    def test_scramble_letter_index_z_position_1(self):
        rotor = EnigmaM3RotorII(1)
        char = "z"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"a","Scramble error")

    def test_scramble_letter_index_a_position_1(self):
        rotor = EnigmaM3RotorII(1)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"j","Scramble error")
    
    def test_scramble_letter_index_a_position_0(self):
        rotor = EnigmaM3RotorII(0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"a","Scramble error")

if __name__ == "__main__":
    unittest.main()