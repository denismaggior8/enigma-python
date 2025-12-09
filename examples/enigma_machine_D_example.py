# Import from this package
from enigmapython.EnigmaDRotorI import EnigmaDRotorI
from enigmapython.EnigmaDRotorII import EnigmaDRotorII
from enigmapython.EnigmaDRotorIII import EnigmaDRotorIII
from enigmapython.EnigmaDEtw_QWERTZ import EnigmaDEtw_QWERTZ
from enigmapython.EnigmaD import EnigmaD
from enigmapython.ReflectorUKW_EnigmaCommercial import ReflectorUKW_EnigmaCommercial

# Import from python ecosystem
import logging
import sys


# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma D components (compared to other machine types, Enigma D doesn't have a plugboard)
rotor1 = EnigmaDRotorI(ring=0,position=0)
rotor2 = EnigmaDRotorI(ring=0,position=0)
rotor3 = EnigmaDRotorI(ring=0,position=0)
reflector = ReflectorUKW_EnigmaCommercial(position=0, ring=0)  # Settable reflector with position and ring
etw = EnigmaDEtw_QWERTZ()

# Setup Enigma D machine
enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)



# Test the Enigma machines
if __name__ == "__main__":

   print(enigma.input_string("a"))