
from string import ascii_lowercase

class Etw:
    wiring = None
    alphabet_list = None

    def process_char_forward(self,char,shift):
        return self.wiring[self.alphabet_list.index(char)+shift]
    
    def process_char_backward(self,char,shift):
        myint = (self.alphabet_list.index(char)-shift) % len(self.alphabet_list)
        myletter = self.alphabet_list[myint]
        myint1 = self.wiring.index(myletter)
        return self.alphabet_list[myint1]
    
    def __init__(self, wiring, alphabet=ascii_lowercase):
        self.wiring = wiring
        self.alphabet_list = list(alphabet)

    def __str__(self):
        return self.wiring