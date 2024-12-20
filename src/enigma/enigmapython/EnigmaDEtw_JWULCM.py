from .Etw import Etw

class EnigmaDEtw_JWULCM(Etw):
    wiring = "jwulcmnohpqzyxiradkegvbtsf"
    def __init__(self):
         super().__init__(self.wiring)