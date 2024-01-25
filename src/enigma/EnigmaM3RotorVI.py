from Rotor import Rotor


class EnigmaM3RotorVI(Rotor):
    
    wiring = 'jpgvoumfyqbenhzrdkasxlictw'
    notch_indexes = [12,25]

    def __init__(self, position):
        super().__init__(self.wiring,position,self.notch_indexes)

