from .Plugboard import Plugboard
from .Alphabets import Alphabets

class PlugboardPassthrough(Plugboard):
   
    def __init__(self, alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase')):
         # Since this is a passthrough plugboard, the wiring is the same as the alphabet
         super().__init__(wiring=alphabet,alphabet=alphabet)
