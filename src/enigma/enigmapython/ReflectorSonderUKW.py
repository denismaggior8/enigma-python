from .Rotor import Rotor

class ReflectorSonderUKW(Rotor):
    
    wiring = 'ciagsndrbytpzfulvhekoqxwjm'
    tag = "IS_UKW"
    
    def __init__(self):
        super().__init__(self.wiring,0)