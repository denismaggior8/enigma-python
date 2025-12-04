from .Etw import Etw

class EtwQWERTZ(Etw):
    """Shared QWERTZ keyboard layout ETW used by Enigma D and Enigma K"""
    wiring = "qwertzuioasdfghjkpyxcvbnml"
    def __init__(self):
         super().__init__(self.wiring)
