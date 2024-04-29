from .Rotor import Rotor

class ReflectorUKWBThin(Rotor):
    
    wiring = 'enkqauywjicopblmdxzvfthrgs'
    tag = "UKW-BT"
    
    def __init__(self):
        super().__init__(self.wiring,0)