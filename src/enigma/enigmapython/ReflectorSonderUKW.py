from .Rotor import Rotor
from .Reflector import Reflector
class ReflectorSonderUKW(Reflector):
    
    wiring = 'ciagsndrbytpzfulvhekoqxwjm'
    tag = "IS_UKW"
    
    def __init__(self):
        super().__init__(self.wiring,0)