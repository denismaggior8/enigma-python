from .Etw import Etw

class EnigmaTEtw(Etw):
    """Entry wheel (ETW) for Enigma T (Tirpitz)"""
    wiring = "kzrouqhyaigblwvstdxfpnmcje"
    def __init__(self):
         super().__init__(self.wiring)
