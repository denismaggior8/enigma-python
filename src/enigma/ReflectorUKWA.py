from Rotor import Rotor

class ReflectorUKWA(Rotor):
    
    wiring = 'ejmzalyxvbwfcrquontspikhgd'
    
    def __init__(self):
        super().__init__(self.wiring,0)