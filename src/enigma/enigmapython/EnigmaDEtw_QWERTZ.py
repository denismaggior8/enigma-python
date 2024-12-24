from .Etw import Etw

class EnigmaDEtw_QWERTZ(Etw):
    wiring = "qwertzuioasdfghjkpyxcvbnml"
    def __init__(self):
         super().__init__(self.wiring)