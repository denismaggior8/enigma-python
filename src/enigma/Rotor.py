from Observable import Observable
import logging

class Rotor(Observable):
    wiring = None
    position = 0
    rotations_counter = 0
    notch_indexes = None
    double_step_triggered = False

    def reset_position(self):
        self.position = 0
    
    def increment_position(self):
        self.position = ((self.position + 1) % len(self.wiring))
        self.rotations_counter = (self.rotations_counter + 1)
        for notch_index in self.notch_indexes:
            logging.debug("Evaluating notch_index {} against position {}".format(notch_index+1,self.position))
            if ((self.position % len(self.wiring)) == ((notch_index+1) % len(self.wiring))):
                logging.debug("Found that rotor position {} is equals to notch {}, notifying observers".format(self.position % len(self.wiring), ((notch_index+1) % len(self.wiring))))
                self.notify_observers(None,None)

    def set_position(self,position):
        self.position = position % len(self.wiring)
        self.rotations_counter = 0
        
    def scramble_letter_index(self, dictionary, letter_index):
        scrambled_letter_index_from_rotor = dictionary.index(dictionary[(self.position + letter_index) % len(dictionary)])
        return dictionary[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position, notch_indexes=[]):
        self.wiring = wiring
        self.position = position % len(wiring)
        self.notch_indexes = notch_indexes

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
    
    def __eq__(self, __value: object) -> bool:
        return id(self) == id(object)
    
