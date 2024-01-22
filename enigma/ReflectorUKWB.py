from .Rotor import Rotor

class ReflectorUKWB(Rotor):
    
    wiring = 'yruhqsldpxngokmiebfzcwvjat'
    
    def __init__(self):
        super().__init__(self.wiring,0)