from .Scrambler import Scrambler

class Reflector(Scrambler):
    tag = None

    def __str__(self):
        str = Scrambler.__str__(self)
        str += "\n"
        str += self.wiring
        return str