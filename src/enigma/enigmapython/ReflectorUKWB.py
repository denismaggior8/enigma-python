from .Rotor import Rotor

class ReflectorUKWB(Rotor):
    
    wiring = 'yruhqsldpxngokmiebfzcwvjat'
    tag = "UKW-B"
    
    def __init__(self):
        super().__init__(self.wiring,0)