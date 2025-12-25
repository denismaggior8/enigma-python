from .Rotor import Rotor

class DynamicNotchRotor(Rotor):
    """
    Rotor that updates its notch position based on the ring setting.
    In Enigma K, the notch is attached to the letter ring (rather than the rotor body).
    Therefore, changing the ring setting shifts the effective notch position relative to the core wiring.
    """
    original_notch_indexes = None

    def __init__(self, wiring, notch_indexes, alphabet, position=0, ring=0):
        # We must save the original notch indexes before calling super().__init__
        # because super().__init__ calls set_ring (via Settable), which we override.
        self.original_notch_indexes = notch_indexes
        super().__init__(wiring, notch_indexes, alphabet, position, ring)
        # Rotor.__init__ sets self.notch_indexes = notch_indexes at the end, 
        # overwriting any changes made by our set_ring during init.
        # So we must call set_ring again to ensure notches are calculated correctly.
        self.set_ring(ring)

    def set_ring(self, ring):
        # First perform standard ring setting (wiring rotation)
        super().set_ring(ring)
        
        # Now adjust notch positions
        # Formula: effective_notch = (notch - ringstellung) mod 26
        # Note: self.wiring can be used for length, or self.alphabet_list
        if self.original_notch_indexes is not None:
            length = len(self.wiring)
            self.notch_indexes = []
            for notch in self.original_notch_indexes:
                new_notch = (notch + ring) % length
                self.notch_indexes.append(new_notch)
