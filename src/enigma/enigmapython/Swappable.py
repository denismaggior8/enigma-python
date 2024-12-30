from .Utils import Utils

class Swappable:
    
    def bulk_swap(self,chars):
        if chars != None and isinstance(chars, dict):
            for key, value in chars.items():
                self.swap(key,value)

    def swap(self, c1, c2):
        if c1 != None and self.wiring.__contains__(c1) and c2 != None and self.wiring.__contains__(c2):
            self.wiring = Utils.swap_chars(self.wiring, c1, c2)