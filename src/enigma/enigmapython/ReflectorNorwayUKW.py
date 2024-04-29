from .Rotor import Rotor

class ReflectorNorwayUKW(Rotor):
    
    wiring = 'mowjypuxndsraibfvlkzgqchet'
    tag = "IN_UKW"
    
    def __init__(self):
        super().__init__(self.wiring,0)