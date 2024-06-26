
from enigmapython.EnigmaIRotorV import EnigmaIRotorV
from string import ascii_lowercase
import unittest

class TestEnigmaIRotorV(unittest.TestCase):
    
    def test_scramble_letter_index_c_position_0(self):
        rotor = EnigmaIRotorV(0)
        char = "c"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"b","Scramble error")

    def test_scramble_letter_index_d_position_0(self):
        rotor = EnigmaIRotorV(0)
        char = "d"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"r","Scramble error")
    
    def test_scramble_letter_index_a_position_0(self):
        rotor = EnigmaIRotorV(0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"v","Scramble error")

if __name__ == "__main__":
    unittest.main()