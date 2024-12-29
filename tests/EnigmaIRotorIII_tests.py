
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from string import ascii_lowercase
import unittest

class TestEnigmaIRotorI(unittest.TestCase):
    
    def test_scramble_letter_index_z_position_1(self):
        rotor = EnigmaIRotorIII(1)
        char = "z"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),rotor.position)
        self.assertEqual(scrambled_char,"b","Scramble error")

    def test_scramble_letter_index_a_position_1(self):
        rotor = EnigmaIRotorIII(1)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),rotor.position)
        self.assertEqual(scrambled_char,"d","Scramble error")
    
    def test_scramble_letter_index_a_position_0(self):
        rotor = EnigmaIRotorIII(0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char),rotor.position)
        self.assertEqual(scrambled_char,"b","Scramble error")

if __name__ == "__main__":
    unittest.main()