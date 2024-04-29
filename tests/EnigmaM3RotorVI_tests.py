
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from string import ascii_lowercase
import unittest

class TestEnigmaM3RotorVI(unittest.TestCase):
    
    def test_scramble_letter_index_c_position_0(self):
        rotor = EnigmaM3RotorVI(0)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"g","Scramble error")

    def test_scramble_letter_index_c_position_1(self):
        rotor = EnigmaM3RotorVI(1)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"v","Scramble error")

    def test_scramble_letter_index_c_position_25(self):
        rotor = EnigmaM3RotorVI(26)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"g","Scramble error")

if __name__ == "__main__":
    unittest.main()