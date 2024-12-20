from .Etw import Etw

class EnigmaDEtw(Etw):
    #wiring = "qwertzuioasdfghjkpyxcvbnml"
    wiring = "jwulcmnohpqzyxiradkegvbtsf"
    def __init__(self):
         super().__init__(self.wiring)