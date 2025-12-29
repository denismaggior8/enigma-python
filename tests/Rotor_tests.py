from enigmapython.Rotor import Rotor
from enigmapython.Alphabets import Alphabets    
import unittest
import random

class TestRotor(unittest.TestCase):

    def test_reset_rotor_position(self):
        rotor = Rotor(alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase'),position=25, turnover_indexes=[], ring=0, wiring=Alphabets.lookup.get('latin_i18n_26chars_lowercase'))
        rotor.reset_position()
        self.assertEqual(rotor.position, 0, "Rotor position is wrong")
         
    def test_set_rotor_position(self):
        rotor = Rotor(alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase'),position=0, turnover_indexes=[],wiring=Alphabets.lookup.get('latin_i18n_26chars_lowercase'))
        random_int = random.randint(0, 10000)
        rotor.set_position(random_int)
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

    def test_set_rotor_negative_position(self):
        rotor = Rotor(alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase'),position=0, turnover_indexes=[], wiring=Alphabets.lookup.get('latin_i18n_26chars_lowercase'))
        random_int = random.randint(-10000, -1)
        rotor.set_position(random_int)
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)
