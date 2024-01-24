from RotorWiringI import RotorWiringI
from string import ascii_lowercase
import unittest
import random

class TestRotorWiringI(unittest.TestCase):
    
    def test_scramble_letter_index_z_position_1(self):
        rotor = RotorWiringI(1)
        char = "z"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")

    def test_scramble_letter_index_a_position_1(self):
        rotor = RotorWiringI(1)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"k","Scramble error")
    
    def test_scramble_letter_index_a_position_0(self):
        rotor = RotorWiringI(0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")
    
    def test_rotor_multiple_position_increment(self):
        rotor = RotorWiringI(0)
        random_int = random.randint(0, 10000)
        for i in range(random_int):
            rotor.increment_position()
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

    def test_rotor_position_increment_by_1(self):
        rotor = RotorWiringI(0)
        rotor.increment_position()
        self.assertEqual(rotor.position, 1, "Rotor position is wrong")

    def test_rotor_position_increment_by_1_over_boundary(self):
        rotor = RotorWiringI(25)
        rotor.increment_position()
        self.assertEqual(rotor.position, 0, "Rotor position is wrong")

if __name__ == "__main__":
    unittest.main()