
from string import ascii_lowercase

class Rotor:
    wiring = None
    position = 0
    
    def increment_position(self):
        self.position = (self.position + 1) % len(self.wiring)

    def set_position(self,position):
        self.position = position % len(self.wiring)
        
    def scramble_letter_index(self, dictionary, letter_index):
        scrambled_letter_index_from_rotor = dictionary.index(dictionary[(self.position + letter_index) % len(dictionary)])
        return dictionary[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = position % len(wiring)

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 