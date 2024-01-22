
from string import ascii_lowercase
import unittest
import random


class Rotor:
    wiring = None
    position = 0
    
    def increment_position(self):
        self.position = ((self.position + 1) % len(self.wiring))

    def set_position(self,position):
        self.position = position % len(self.wiring)
        
    def scramble_letter_index(self, dictionary, letter_index):
        scrambled_letter_index_from_rotor = dictionary.index(dictionary[(self.position + letter_index) % len(dictionary)])
        return dictionary[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position):
        if wiring == None:
            wiring = list(ascii_lowercase)
        self.wiring = wiring
        self.position = position % len(wiring)

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
    
class TestRotor(unittest.TestCase):
    
    def test_rotor_position_increment_by_1(self):
        rotor = Rotor(None,0)
        rotor.increment_position()
        self.assertEqual(rotor.position, 1, "Rotor position is wrong")
    
    def test_rotor_multiple_position_increment(self):
        rotor = Rotor(None,0)
        random_int = random.randint(0, 10000)
        for i in range(random_int):
            rotor.increment_position()
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")
    
    def test_set_rotor_position(self):
        rotor = Rotor(None,0)
        random_int = random.randint(0, 10000)
        rotor.set_position(random_int)
        self.assertEqual(rotor.position, random_int % len(rotor.wiring), "Rotor position is wrong")

unittest.main()