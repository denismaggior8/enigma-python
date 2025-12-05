import logging
from .Journaled import Journaled

class Scrambler(Journaled):
    wiring = None
    alphabet_list = None
    original_wiring = None

    def scramble_char(self, dictionary, letter_index, shift): 
        output_char_index = dictionary.index(dictionary[(shift + letter_index) % len(dictionary)])
        output_char = dictionary[output_char_index]
        super().append_to_journal({
            'output_char': output_char
        })
        return output_char
    
    def __init__(self, wiring, alphabet):
        #Journaled.__init__(self)
        super().__init__()
        self.wiring = wiring
        self.original_wiring = self.wiring
        self.alphabet_list = list(alphabet)
 
    def __str__(self):
        str = ""
        for char in self.alphabet_list:
            str += char
        str += "\n"
        str += "|" * len(self.alphabet_list)
        return str