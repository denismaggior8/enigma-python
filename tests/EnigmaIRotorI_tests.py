from EnigmaIRotorI import EnigmaIRotorI
from string import ascii_lowercase
import unittest
import random

class TestEnigmaIRotorI(unittest.TestCase):
    
    def test_scramble_letter_index_z_position_1(self):
        rotor = EnigmaIRotorI(1)
        char = "z"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")

    def test_scramble_letter_index_a_position_1(self):
        rotor = EnigmaIRotorI(1)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"k","Scramble error")
    
    def test_scramble_letter_index_a_position_0(self):
        rotor = EnigmaIRotorI(0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")
    
    def test_rotor_multiple_position_increment(self):
        rotor = EnigmaIRotorI(0)
        random_int = random.randint(0, 10000)
        for i in range(random_int):
            rotor.increment_position()
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

    def test_rotor_position_increment_by_1(self):
        rotor = EnigmaIRotorI(0)
        rotor.increment_position()
        self.assertEqual(rotor.position, 1, "Rotor position is wrong")

    def test_rotor_position_increment_by_1_over_boundary(self):
        rotor = EnigmaIRotorI(25)
        rotor.increment_position()
        self.assertEqual(rotor.position, 0, "Rotor position is wrong")

    def test_rotor_ring_position_1(self):
        rotor = EnigmaIRotorI(position = 0, ring = 1)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"k","Scramble error")

    def test_rotor_ring_position_26(self):
        rotor = EnigmaIRotorI(position = 0, ring = 26)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")

    def test_rotor_ring_position_0(self):
        rotor = EnigmaIRotorI(position = 0, ring = 0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")


if __name__ == "__main__":
    unittest.main()