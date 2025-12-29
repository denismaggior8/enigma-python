from .Rotor import Rotor

class DynamicTurnoverRotor(Rotor):
    """
    Rotor that updates its notch position based on the ring setting using the formula:
    effective_notch = (notch + ringstellung) mod 26
    """
    original_turnover_indexes = None

    def __init__(self, wiring, turnover_indexes, alphabet, position=0, ring=0, turnover_function=None):
        # We must save the original notch indexes before calling super().__init__
        # because super().__init__ calls set_ring (via Settable), which we override.
        self.original_turnover_indexes = turnover_indexes
        
        if turnover_function is None:
            self.turnover_function = lambda notch, ring, length: (notch + ring) % length
        else:
            self.turnover_function = turnover_function
            
        super().__init__(wiring, turnover_indexes, alphabet, position, ring)
        # Rotor.__init__ sets self.turnover_indexes = turnover_indexes at the end, 
        # overwriting any changes made by our set_ring during init.
        # So we must call set_ring again to ensure notches are calculated correctly.
        self.set_ring(ring)

    def set_ring(self, ring):
        # First perform standard ring setting (wiring rotation)
        super().set_ring(ring)
        
        # Now adjust notch positions using the turnover function
        if self.original_turnover_indexes is not None:
            length = len(self.wiring)
            self.turnover_indexes = []
            for notch in self.original_turnover_indexes:
                new_notch = self.turnover_function(notch, ring, length)
                self.turnover_indexes.append(new_notch)
