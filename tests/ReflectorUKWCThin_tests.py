
from enigmapython.ReflectorUKWCThin import ReflectorUKWCThin
from enigmapython.Alphabets import Alphabets
import unittest

class TestReflectorUKWCThin(unittest.TestCase):
    
    def test_reflector_b_scramble_letter_index_z(self):
        reflector = ReflectorUKWCThin()
        char = "z"
        scrambled_char = reflector.scramble_letter_index(reflector.wiring,Alphabets.lookup.get('latin_i18n_26chars_lowercase').index(char),0)
        self.assertEqual(scrambled_char,"q","Scramble error")

if __name__ == "__main__":
    unittest.main()