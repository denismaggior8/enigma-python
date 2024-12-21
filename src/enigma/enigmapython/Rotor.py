from .Observable import Observable
from .Utils import Utils
from string import ascii_lowercase
import logging

class Rotor(Observable):
    original_wiring = None
    wiring = None
    position = None
    rotations_counter = None
    notch_indexes = None
    double_step_triggered = None
    ring = None
    dot_position = None
    lookup = {}
    alphabet = None

    @staticmethod
    def register(tag, class_name):
        Rotor.lookup[tag] = class_name

    def reset_position(self):
        self.position = 0
    
    def increment_position(self):
        self.position = ((self.position + 1) % len(self.wiring))
        self.rotations_counter = self.rotations_counter + 1
        for notch_index in self.notch_indexes:
            logging.debug("Evaluating notch_index {} against position {}".format(notch_index+1,self.position))
            if (self.position == ((notch_index+1) % len(self.wiring))):
                logging.debug("Found that rotor position {} is equals to notch {}, notifying observers".format(self.position, ((notch_index+1) % len(self.wiring))))
                self.notify_observers(None,None)

    def set_position(self,position):
        self.position = position % len(self.wiring)
        self.rotations_counter = 0
        
    def scramble_letter_index(self, dictionary, letter_index):
        scrambled_letter_index_from_rotor = dictionary.index(dictionary[(self.position + letter_index) % len(dictionary)])
        return dictionary[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position = 0, ring = 0, notch_indexes=[], alphabet=ascii_lowercase):
        self.wiring = wiring
        self.position = position % len(wiring)
        self.notch_indexes = notch_indexes
        self.double_step_triggered = False
        self.rotations_counter = 0
        self.original_wiring = self.wiring
        self.ring = ring
        self.alphabet = list(alphabet)
        self.set_rotor_ring(ring)

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
    
    def __eq__(self, __value: object) -> bool:
        return id(self) == id(object)

    def set_rotor_ring(self, ring):
        self.wiring = self.original_wiring
        self.dot_position = list(self.wiring).index("a")
        logging.debug("Dot position: " + str(self.dot_position))
        for i in range(0, ring):
        # Set temporary wiring variable
            temp_wiring = self.wiring
            # Set actual wiring to empty string
            wiring = ""
            # Loop over chars in temporary wiring
            for char in temp_wiring:
                # Shift the char by one and add that shifted char to wiring variable
                wiring += Rotor.shift(char, 1, self.alphabet)
            # Add one to dot position, make sure we don't exceed the lenght of the alphabet
            self.wiring = wiring
            self.dot_position = (self.dot_position + 1) % len(self.alphabet)
            logging.debug("Wiring shifted up the alphabet: " + wiring)
            logging.debug("New dot position: " + str(self.dot_position))
        i = 0
        # While the letter at the dot position doesn't match with the ringstellung
        while not self.wiring[self.dot_position] == self.alphabet[ring % len(self.wiring)]:
            i += 1
            # Rotate the wiring
            self.wiring = self.wiring[-1:] + self.wiring[:-1]
            logging.debug("Rotation " + str(i).zfill(2) + "; Wiring: " + self.wiring)
         
    @staticmethod
    def shift(letter, shift, alphabet_list):
        for i in range(0, len(alphabet_list)):
            if alphabet_list[i] == letter:
                return alphabet_list[(i + shift) % len(alphabet_list)]
            
    @staticmethod
    def get_instance_from_tag(tag: str):
        return Utils.get_class_instance(Rotor.lookup[tag].__module__+"."+Rotor.lookup[tag].__name__)()