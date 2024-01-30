
from ReflectorUKWCThin import ReflectorUKWCThin
from string import ascii_lowercase
import unittest

class TestReflectorUKWCThin(unittest.TestCase):
    
    def test_reflector_b_scramble_letter_index_z(self):
        reflector = ReflectorUKWCThin()
        char = "z"
        scrambled_char = reflector.scramble_letter_index(reflector.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"q","Scramble error")

if __name__ == "__main__":
    unittest.main()