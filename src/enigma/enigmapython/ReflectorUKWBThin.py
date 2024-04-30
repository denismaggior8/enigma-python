from .Rotor import Rotor
from .Reflector import Reflector
class ReflectorUKWBThin(Reflector):
    
    wiring = 'enkqauywjicopblmdxzvfthrgs'
    tag = "UKW-BT"
    
    def __init__(self):
        super().__init__(self.wiring,0)