
from enigmapython.ReflectorUKWB import ReflectorUKWB
from string import ascii_lowercase
import unittest

class TestReflectorUKWB(unittest.TestCase):
    
    def test_reflector_b_scramble_letter_index_z(self):
        reflector = ReflectorUKWB()
        char = "z"
        scrambled_char = reflector.scramble_letter_index(reflector.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"t","Scramble error")

if __name__ == "__main__":
    unittest.main()