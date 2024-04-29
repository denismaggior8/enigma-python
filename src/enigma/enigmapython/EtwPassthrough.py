from .Etw import Etw

class EtwPassthrough(Etw):
    wiring = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
         super().__init__(self.wiring)