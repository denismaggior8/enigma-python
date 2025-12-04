from .Etw import Etw

class EtwJWULCM(Etw):
    """Shared JWULCM keyboard layout ETW used by Enigma D"""
    wiring = "jwulcmnohpqzyxiradkegvbtsf"
    def __init__(self):
         super().__init__(self.wiring)
