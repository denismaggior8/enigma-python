from Rotor import Rotor
from string import ascii_lowercase
import unittest
import random


class TestRotor(unittest.TestCase):

    def test_reset_rotor_position(self):
        rotor = Rotor(list(ascii_lowercase),25)
        rotor.reset_position()
        self.assertEqual(rotor.position, 0, "Rotor position is wrong")
         
    def test_set_rotor_position(self):
        rotor = Rotor(list(ascii_lowercase),0)
        random_int = random.randint(0, 10000)
        rotor.set_position(random_int)
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

    def test_set_rotor_negative_position(self):
        rotor = Rotor(list(ascii_lowercase),0)
        random_int = random.randint(-10000, -1)
        rotor.set_position(random_int)
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)
