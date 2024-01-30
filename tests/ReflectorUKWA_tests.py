
from ReflectorUKWA import ReflectorUKWA
from string import ascii_lowercase
import unittest

class TestReflectorUKWA(unittest.TestCase):
    
    def test_reflector_b_scramble_letter_index_z(self):
        reflector = ReflectorUKWA()
        char = "z"
        scrambled_char = reflector.scramble_letter_index(reflector.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"d","Scramble error")

if __name__ == "__main__":
    unittest.main()