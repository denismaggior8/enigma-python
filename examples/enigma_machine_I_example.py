# Import from this package
from enigmapython.EnigmaIRotorI import EnigmaIRotorI
from enigmapython.EnigmaIRotorII import EnigmaIRotorII
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaI import EnigmaI

# Import from python ecosystem
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma I components
plugboard = PlugboardPassthrough()
rotor1 = EnigmaIRotorI(ring=0,position=0)
rotor2 = EnigmaIRotorII(ring=0,position=0)
rotor3 = EnigmaIRotorIII(ring=0,position=0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

# Setup Enigma I machine
enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)

# Test the Enigma machine
if __name__ == "__main__":
   
   print(enigma.input_char("c"))
   print(enigma.input_char("i"))
   print(enigma.input_char("a"))
   print(enigma.input_char("o"))
   
   print(enigma.input_string("supercalifragilistichespiralidoso"))
