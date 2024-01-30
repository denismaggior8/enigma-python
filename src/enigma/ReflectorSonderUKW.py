from Rotor import Rotor

class ReflectorSonderUKW(Rotor):
    
    wiring = 'ciagsndrbytpzfulvhekoqxwjm'
    
    def __init__(self):
        super().__init__(self.wiring,0)