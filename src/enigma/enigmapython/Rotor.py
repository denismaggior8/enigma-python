from .Observable import Observable
from .Scrambler import Scrambler
import logging

class Rotor(Scrambler,Observable):
    position = None
    rotations_counter = None
    notch_indexes = None
    double_step_triggered = None

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

    def __init__(self, wiring, notch_indexes, alphabet, position = 0, ring = 0):
        # Scrambler properties
        super().__init__(
            wiring = wiring,
            ring = ring,
            alphabet = alphabet
        )
        # Rotor properties
        self.position = position % len(wiring)
        self.notch_indexes = notch_indexes
        self.double_step_triggered = False
        self.rotations_counter = 0
        


    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
    
    def __eq__(self, __value: object) -> bool:
        return id(self) == id(object)

 
            