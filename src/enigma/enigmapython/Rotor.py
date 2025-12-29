from .Observable import Observable
from .Scrambler import Scrambler
from .Settable import Settable
import logging

class Rotor(Scrambler,Observable,Settable):
    rotations_counter = None
    turnover_indexes = None
    double_step_triggered = None

    def increment_position(self):
        self.position = ((self.position + 1) % len(self.wiring))
        self.rotations_counter = self.rotations_counter + 1
        for turnover_index in self.turnover_indexes:
            logging.debug("Evaluating turnover_index {} against position {}".format(turnover_index+1,self.position))
            if (self.position == ((turnover_index+1) % len(self.wiring))):
                logging.debug("Found that rotor position {} is equals to notch {}, notifying observers".format(self.position, ((turnover_index+1) % len(self.wiring))))
                self.notify_observers(None,None)

    def set_position(self,position):
        super().set_position(position % len(self.wiring))
        self.rotations_counter = 0

    def __init__(self, wiring, turnover_indexes, alphabet, position = 0, ring = 0):
        # Scrambler properties
        Scrambler.__init__(self, wiring=wiring, alphabet=alphabet)
        # Settable properties
        Settable.__init__(self, position=position % len(wiring), ring=ring)
        self.set_ring(self.ring)
        
        # Rotor properties
        self.turnover_indexes = turnover_indexes
        self.double_step_triggered = False
        self.rotations_counter = 0
        


    def __str__(self):
        str = Scrambler.__str__(self)
        str += "\n"
        # Slice the wiring, in order to left-rotate it according to the position
        n = self.position % len(self.wiring)
        str += self.wiring[n:] + self.wiring[:n]
        return str
        
    
    def __eq__(self, __value: object) -> bool:
        return id(self) == id(object)

 
            