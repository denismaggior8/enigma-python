from .Plugboard import Plugboard

class PlugboardPassthrough(Plugboard):
    wiring = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
         super().__init__(self.wiring)
