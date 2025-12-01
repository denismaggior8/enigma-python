# Import from this package
from enigmapython.EnigmaINorwayRotorI import EnigmaINorwayRotorI
from enigmapython.EnigmaINorwayRotorII import EnigmaINorwayRotorII
from enigmapython.EnigmaINorwayRotorIII import EnigmaINorwayRotorIII
from enigmapython.ReflectorNorwayUKW import ReflectorNorwayUKW
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaINorway import EnigmaINorway

# Import from python ecosystem
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma I Norway components
plugboard = PlugboardPassthrough()
rotor1 = EnigmaINorwayRotorI(ring=0,position=0)
rotor2 = EnigmaINorwayRotorII(ring=0,position=0)
rotor3 = EnigmaINorwayRotorIII(ring=0,position=0)
reflector = ReflectorNorwayUKW()
etw = EtwPassthrough()

# Setup Enigma I Norway machine
enigma = EnigmaINorway(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)

# Test the Enigma machine
if __name__ == "__main__":
   
   print(enigma.input_char("c"))
   print(enigma.input_char("i"))
   print(enigma.input_char("a"))
   print(enigma.input_char("o"))
   
   print(enigma.input_string("supercalifragilistichespiralidoso"))
