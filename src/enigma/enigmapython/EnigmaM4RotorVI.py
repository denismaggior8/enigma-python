from .Rotor import Rotor
from .Alphabets import Alphabets 

class EnigmaM4RotorVI(Rotor):

    wiring = 'jpgvoumfyqbenhzrdkasxlictw'
    notch_indexes = [12,25]

    tag = "M4_VI"

    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            notch_indexes=self.notch_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )

