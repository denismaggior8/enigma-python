from .Rotor import Rotor

class ReflectorUKWA(Rotor):
    
    wiring = 'ejmzalyxvbwfcrquontspikhgd'
    tag = "UKW-A"
    
    def __init__(self):
        super().__init__(self.wiring,0)