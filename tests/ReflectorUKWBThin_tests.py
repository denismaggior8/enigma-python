
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from string import ascii_lowercase
import unittest

class TestReflectorUKWBThin(unittest.TestCase):
    
    def test_reflector_b_scramble_letter_index_z(self):
        reflector = ReflectorUKWBThin()
        char = "z"
        scrambled_char = reflector.scramble_letter_index(reflector.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"s","Scramble error")

if __name__ == "__main__":
    unittest.main()