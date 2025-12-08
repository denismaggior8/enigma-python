class Settable:
    position = 0
    ring = 0
    
    def __init__(self, position=0, ring=0):
        self.position = position
        self.ring = ring

    def set_position(self, position):
        self.position = position
        
    def reset_position(self):
        self.position = 0
        
    def reset_ring(self):
        self.set_ring(0)
        
    def set_ring(self, ring):
        self.ring = ring
        self.wiring = self.original_wiring
        self.dot_position = list(self.wiring).index(self.alphabet_list[0])
        import logging
        logging.debug("Dot position: " + str(self.dot_position))
        for i in range(0, ring):
        # Set temporary wiring variable
            temp_wiring = self.wiring
            # Set actual wiring to empty string
            wiring = ""
            # Loop over chars in temporary wiring
            for char in temp_wiring:
                # Shift the char by one and add that shifted char to wiring variable
                wiring += self._shift(char, 1, self.alphabet_list)
            # Add one to dot position, make sure we don't exceed the lenght of the alphabet
            self.wiring = wiring
            self.dot_position = (self.dot_position + 1) % len(self.alphabet_list)
            logging.debug("Wiring shifted up the alphabet: " + wiring)
            logging.debug("New dot position: " + str(self.dot_position))
        i = 0
        # While the letter at the dot position doesn't match with the ringstellung
        while not self.wiring[self.dot_position] == self.alphabet_list[ring % len(self.wiring)]:
            i += 1
            # Rotate the wiring
            self.wiring = self.wiring[-1:] + self.wiring[:-1]
            # The following line has been commente out becode not Micropython compatible
            # logging.debug("Rotation " + str(i).zfill(2) + "; Wiring: " + self.wiring)

    @staticmethod
    def _shift(letter, shift, alphabet_list):
        for i in range(0, len(alphabet_list)):
            if alphabet_list[i] == letter:
                return alphabet_list[(i + shift) % len(alphabet_list)]
