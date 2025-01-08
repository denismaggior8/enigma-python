
from enigmapython.EnigmaIRotorV import EnigmaIRotorV
from string import ascii_lowercase
import unittest

class TestEnigmaIRotorV(unittest.TestCase):
    
    def test_scramble_char_c_position_0(self):
        rotor = EnigmaIRotorV(0)
        char = "c"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"b","Scramble error")

    def test_scramble_char_d_position_0(self):
        rotor = EnigmaIRotorV(0)
        char = "d"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"r","Scramble error")
    
    def test_scramble_char_a_position_0(self):
        rotor = EnigmaIRotorV(0)
        char = "a"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"v","Scramble error")

if __name__ == "__main__":
    unittest.main()