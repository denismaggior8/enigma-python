from enigmapython.EnigmaB_A133RotorI import EnigmaB_A133RotorI
from enigmapython.EnigmaB_A133RotorII import EnigmaB_A133RotorII
from enigmapython.EnigmaB_A133RotorIII import EnigmaB_A133RotorIII
from enigmapython.EnigmaB_A133Etw import EnigmaB_A133Etw
from enigmapython.EnigmaB_A133 import EnigmaB_A133
from enigmapython.ReflectorUKW_EnigmaB_A133 import ReflectorUKW_EnigmaB_A133

# Import from python ecosystem
import logging
import sys


# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma B components (compared to other machine types, Enigma B doesn't have a plugboard)
rotor1 = EnigmaB_A133RotorI(0)
rotor2 = EnigmaB_A133RotorI(0)
rotor3 = EnigmaB_A133RotorI(0)
reflector = ReflectorUKW_EnigmaB_A133()
etw = EnigmaB_A133Etw()


# Setup Enigma B machine
enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)



# Test the Enigma machines
if __name__ == "__main__":

   print(enigma.input_string("ettbesettbesettbesettbesettbesettbesettbesettbesettbesettbesettbesettbes"))