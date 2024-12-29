
from enigmapython.EnigmaM3RotorVII import EnigmaM3RotorVII
from string import ascii_lowercase
import unittest

class TestEnigmaM3RotorVII(unittest.TestCase):
    
    def test_scramble_letter_index_c_position_0(self):
        rotor = EnigmaM3RotorVII(0)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"j","Scramble error")

    def test_scramble_letter_index_c_position_1(self):
        rotor = EnigmaM3RotorVII(1)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"h","Scramble error")

    def test_scramble_letter_index_c_position_25(self):
        rotor = EnigmaM3RotorVII(26)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"j","Scramble error")

if __name__ == "__main__":
    unittest.main()