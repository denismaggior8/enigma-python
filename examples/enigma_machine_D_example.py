# Import from this package
from enigmapython.EnigmaDRotorI import EnigmaDRotorI
from enigmapython.EnigmaDRotorII import EnigmaDRotorII
from enigmapython.EnigmaDRotorIII import EnigmaDRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EnigmaDEtw import EnigmaDEtw
from enigmapython.EnigmaD import EnigmaD
from enigmapython.ReflectorDUKW import ReflectorDUKW

# Import from python ecosystem
import logging
import sys


# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma D components
plugboard = PlugboardPassthrough()
rotor1 = EnigmaDRotorI()
rotor2 = EnigmaDRotorI()
rotor3 = EnigmaDRotorI()
reflector = ReflectorDUKW()
etw = EnigmaDEtw()

# Setup Enigma D machine
enigma = EnigmaD(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)



# Test the Enigma machines
if __name__ == "__main__":

   print(enigma.input_string("a"))