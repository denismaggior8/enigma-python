import logging
from .Journaled import Journaled

class Scrambler(Journaled):
    wiring = None
    alphabet_list = None
    dot_position = None
    ring = None
    set_scrambler_ring = None
    original_wiring = None

    def scramble_char(self, dictionary, letter_index, shift): 
        output_char_index = dictionary.index(dictionary[(shift + letter_index) % len(dictionary)])
        output_char = dictionary[output_char_index]
        super().append_to_journal({
            'output_char': output_char
        })
        return output_char
    
    def __init__(self, wiring, alphabet, ring):
        #Journaled.__init__(self)
        super().__init__()
        self.wiring = wiring
        self.original_wiring = self.wiring
        self.alphabet_list = list(alphabet)
        self.ring = ring
        self.set_scrambler_ring(ring)
        
        
    def set_scrambler_ring(self, ring):
        self.wiring = self.original_wiring
        self.dot_position = list(self.wiring).index(self.alphabet_list[0])
        logging.debug("Dot position: " + str(self.dot_position))
        for i in range(0, ring):
        # Set temporary wiring variable
            temp_wiring = self.wiring
            # Set actual wiring to empty string
            wiring = ""
            # Loop over chars in temporary wiring
            for char in temp_wiring:
                # Shift the char by one and add that shifted char to wiring variable
                wiring += Scrambler.__shift(char, 1, self.alphabet_list)
            # Add one to dot position, make sure we don't exceed the lenght of the alphabet
            self.wiring = wiring
            self.dot_position = (self.dot_position + 1) % len(self.alphabet_list)
            logging.debug("Wiring shifted up the alphabet: " + wiring)
            logging.debug("New dot position: " + str(self.dot_position))
        i = 0
        # While the letter at the dot position doesn't match with the ringstellung
        while not self.wiring[self.dot_position] == self.alphabet_list[ring % len(self.wiring)]:
            i += 1
            # Rotate the wiring
            self.wiring = self.wiring[-1:] + self.wiring[:-1]
            logging.debug("Rotation " + str(i).zfill(2) + "; Wiring: " + self.wiring)
         
    @staticmethod
    def __shift(letter, shift, alphabet_list):
        for i in range(0, len(alphabet_list)):
            if alphabet_list[i] == letter:
                return alphabet_list[(i + shift) % len(alphabet_list)]
            
    def __str__(self):
        return self.wiring