
from enigmapython.EnigmaM3RotorVIII import EnigmaM3RotorVIII
from string import ascii_lowercase
import unittest

class TestEnigmaM3RotorVI(unittest.TestCase):
    
    def test_scramble_letter_index_c_position_0(self):
        rotor = EnigmaM3RotorVIII(0)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),rotor.position)
        self.assertEqual(scrambled_char,"q","Scramble error")

    def test_scramble_letter_index_c_position_1(self):
        rotor = EnigmaM3RotorVIII(1)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),rotor.position)
        self.assertEqual(scrambled_char,"h","Scramble error")

    def test_scramble_letter_index_c_position_25(self):
        rotor = EnigmaM3RotorVIII(26)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),rotor.position)
        self.assertEqual(scrambled_char,"q","Scramble error")

if __name__ == "__main__":
    unittest.main()