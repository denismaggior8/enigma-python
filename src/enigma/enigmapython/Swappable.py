from .Utils import Utils

class Swappable:
    
    def bulk_swap(self,chars):
        if chars is not None and isinstance(chars, dict):
            for key, value in chars.items():
                self.swap(key,value)

    def swap(self, c1, c2):
        if c1 is not None and c1 in self.wiring and c2 is not None and c2 in self.wiring:
            self.wiring = Utils.swap_chars(self.wiring, c1, c2)