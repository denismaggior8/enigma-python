from enigmapython.EnigmaIRotorI import EnigmaIRotorI
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
        self.assertEqual(rotor.wiring,"ekmflgdqvzntowyhxuspaibrcj","Wiring error")
        self.assertEqual(scrambled_char,"e","Scramble error")

    def test_rotor_ring_position_0(self):
        rotor = EnigmaIRotorI(position = 0, ring = 0)
        char = "a"
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index(char))
        self.assertEqual(scrambled_char,"e","Scramble error")

    def test_rotor_ring_position_2(self):
        rotor = EnigmaIRotorI(position = 0, ring = 2)
        self.assertEqual(rotor.wiring,"elgmohnifsxbpvqyajzwurckdt","Wiring error")
        self.assertEqual(rotor.dot_position,22,"Dot position error")

    def test_rotor_ring_position_20(self):
        rotor = EnigmaIRotorI(position = 0, ring = 20)
        self.assertEqual(rotor.dot_position,(20+rotor.ring) % len(rotor.wiring),"Dot position error")
  
    def test_rotor_changing_ring_position_0(self):
        rotor = EnigmaIRotorI(position = 0, ring = 0)
        self.assertEqual(rotor.wiring,"ekmflgdqvzntowyhxuspaibrcj","Wiring error")
        self.assertEqual(rotor.dot_position,20,"Dot position error")
        rotor.set_rotor_ring(1)   
        self.assertEqual(rotor.wiring,"kflngmherwaoupxziyvtqbjcsd","Wiring error")
        self.assertEqual(rotor.dot_position,21,"Dot position error")
        rotor.set_rotor_ring(0)
        self.assertEqual(rotor.wiring,"ekmflgdqvzntowyhxuspaibrcj","Wiring error")
        self.assertEqual(rotor.dot_position,20,"Dot position error")
    
    def test_rotor_set_position_and_ring_position(self):
        rotor = EnigmaIRotorI(position = 0, ring = 0)
        self.assertEqual(rotor.wiring,"ekmflgdqvzntowyhxuspaibrcj","Wiring error")
        self.assertEqual(rotor.dot_position,20,"Dot position error")
        rotor.set_rotor_ring(1)   
        self.assertEqual(rotor.wiring,"kflngmherwaoupxziyvtqbjcsd","Wiring error")
        self.assertEqual(rotor.dot_position,21,"Dot position error")
        rotor.set_position(26)
        scrambled_char = rotor.scramble_letter_index(rotor.wiring,list(ascii_lowercase).index('z'))
        self.assertEqual(scrambled_char,"d","Scramble error")
       


if __name__ == "__main__":
    unittest.main()