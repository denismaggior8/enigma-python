
from Observable import Observable
from string import ascii_lowercase
import unittest
import random


class Rotor(Observable):
    wiring = None
    position = 0
    rotations_counter = 0

    def reset_position(self):
        self.position = 0
    
    def increment_position(self):
        self.position = ((self.position + 1) % len(self.wiring))
        self.rotations_counter = ((self.rotations_counter + 1))
        #self.rotations_counter = ((self.rotations_counter + 1)% len(self.wiring))
        if (self.rotations_counter % len(self.wiring)) == 17:
        #if (self.rotations_counter) == 17:
            self.notify_observers("ciao","ciao")

    def set_position(self,position):
        self.position = position % len(self.wiring)
        self.rotations_counter = 0
        
    def scramble_letter_index(self, dictionary, letter_index):
        scrambled_letter_index_from_rotor = dictionary.index(dictionary[(self.position + letter_index) % len(dictionary)])
        return dictionary[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = position % len(wiring)

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
    
class TestRotor(unittest.TestCase):

    def test_reset_rotor_position(self):
        rotor = Rotor(list(ascii_lowercase),25)
        rotor.reset_position()
        self.assertEqual(rotor.position, 0, "Rotor position is wrong")

    def test_rotor_position_increment_by_1(self):
        rotor = Rotor(list(ascii_lowercase),0)
        rotor.increment_position()
        self.assertEqual(rotor.position, 1, "Rotor position is wrong")

    def test_rotor_position_increment_by_1_over_boundary(self):
        rotor = Rotor(list(ascii_lowercase),25)
        rotor.increment_position()
        self.assertEqual(rotor.position, 0, "Rotor position is wrong")
    
    def test_rotor_multiple_position_increment(self):
        rotor = Rotor(list(ascii_lowercase),0)
        random_int = random.randint(0, 10000)
        for i in range(random_int):
            rotor.increment_position()
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")
    
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
    unittest.main()
