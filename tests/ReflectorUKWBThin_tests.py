
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from string import ascii_lowercase
import unittest

class TestReflectorUKWBThin(unittest.TestCase):
    
    def test_reflector_b_scramble_char_z(self):
        reflector = ReflectorUKWBThin()
        char = "z"
        scrambled_char = reflector.scramble_char(reflector.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"s","Scramble error")

if __name__ == "__main__":
    unittest.main()