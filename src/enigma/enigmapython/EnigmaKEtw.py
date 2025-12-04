from .Etw import Etw

class EnigmaKEtw(Etw):
    wiring = "qwertzuioasdfghjkpyxcvbnml"
    def __init__(self):
         super().__init__(self.wiring)
